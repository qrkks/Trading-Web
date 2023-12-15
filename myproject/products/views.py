from django.shortcuts import render
from typing import Any, Dict
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from render_block import render_block_to_string
from django.middleware.csrf import get_token

from abstractapp.custom_context_processors import global_context
from .models import Category, Product

# Create your views here.


def products_index(request):
    """
    This function retrieves the root nodes from the Category model and 
    fetches the active products for each root node. It then prepares the 
    data to be rendered in the template and returns the appropriate response.
    """

    # Retrieve the lever 1 nodes from the Category mptt model
    level_1_nodes = Category.objects.filter(level=1)

    level_1_nodes_data = {}

    # Iterate over each root node
    for category in level_1_nodes:
        # Get all descendants of the category, including itself
        all_category = category.get_descendants(include_self=True)

        # Get the active products that belong to the category and its descendants
        products = Product.objects.active().filter(
            Q(category__in=all_category)
        )[:2]

        # Store the products in the root_nodes_data dictionary
        level_1_nodes_data[category] = products

    # Prepare the context data for rendering the template
    context_data = {
        'root_nodes_data': level_1_nodes_data,
        'partial_template_path': 'products/partial/main-index.html',
    }

    # Check if the request is an HX-Request
    if request.headers.get('HX-Request') == 'true':
        # Render the template block to a string and return the HTML response
        html = render_block_to_string(
            'products/product-index.html', 'content', {**context_data, **global_context(request)})
        return HttpResponse(html)

    # Render the template and return the response
    return render(request, 'products/product-index.html', context_data)


class CategoryProductListView(ListView):
    template_name = 'products/product.html'  # 指定模板文件路径
    context_object_name = 'products'  # 指定模板上下文变量的名称
    paginate_by = 9
    extra_context = {
        'partial_template_path': "products/partial/main-list.html",
        # 'main_title': category_name,
    }

    def get_queryset(self):
        # 获取 category_path 参数并拆分为 slugs 列表
        category_path = self.kwargs['category_path']

        # if category_path == 'all-products':
        #     products = Product.objects.active().all()
        # else:
        category_path_list: list = category_path.split('/')
        category_slug: str = category_path_list.pop()
        # 获取 Category 对象
        category: Category = get_object_or_404(
            Category, slug=category_slug)

        # 使用 Q 对象来构建查询，包括类别及其所有子类别的产品
        products = Product.objects.active().filter(
            Q(category__in=category.get_descendants(include_self=True))
        )

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 然后添加csrf_token到上下文中
        context['csrf_token'] = get_token(self.request)

        # 获取当前类别
        category_path = self.kwargs['category_path']
        slugs = category_path.split('/')
        category_slug = slugs[-1]  # 获取最后一个 slug 作为当前类别的 slug
        category = get_object_or_404(Category, slug=category_slug)  # 获取当前类别对象

        # 构建面包屑
        breadcrumbs = []
        for ancestor in category.get_ancestors(include_self=True):
            breadcrumbs.append(
                {'name': ancestor.name, 'url': ancestor.get_absolute_url()})
        context['breadcrumbs'] = breadcrumbs

        # 添加标题 - 类别名
        context['main_title'] = category.name

        return context

    def render_to_response(self, context, **response_kwargs):
        """
        Renders a response based on the request headers.

        Args:
            context (dict): The context to be passed to the rendered templates.
            response_kwargs (dict): Additional keyword arguments to be passed to the response.

        Returns:
            HttpResponse: The rendered response.

        """
        if self.request.headers.get('HX-Request') == 'true':
            # Check if the request is an HX-Request from the navBar source
            if self.request.headers.get('source') == 'navBar':
                # Render the product.html template with the 'content' block and the context
                return HttpResponse(render_block_to_string('products/product.html',
                                                           'content',
                                                           {**context, **global_context(self.request)}))
            # Handle HX-Request by rendering only the main-list.html template with the context
            return render(self.request, 'products/partial/main-list.html', context)
        else:
            # Handle regular requests by rendering the entire page with the context
            return super().render_to_response(context, **response_kwargs)


class ProductDetail(DetailView):
    template_name = 'products/product.html'
    model = Product
    context_object_name = 'product'
    # slug_field = 'slug'
    extra_context = {
        'partial_template_path': "products/partial/main-detail.html"
    }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Get the context data for the view.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            Dict[str, Any]: The context data.
        """
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        request = self.request
        object = context['object']
        category = object.category

        context['csrf_token'] = get_token(request)

        images = object.images.filter(is_for_display=True)

        attribute_names = [field.name for field in Product._meta.get_fields()]

        filtered_attribute_names = [
            attr for attr in attribute_names if not (
                attr.startswith("page") or
                attr.startswith('is') or
                attr in ['images', 'custom_order', 'detail_description']
            )
        ]

        product_data = {
            attr.replace("_", " "): getattr(object, attr)
            for attr in filtered_attribute_names
        }

        context.update({'product_data': product_data, 'images': images})

        previous_object = (
            Product.objects
            .filter(category=category)
            .filter(id__lt=object.id)
            .order_by('-id')
            .first()
        )
        next_object = (
            Product.objects
            .filter(category=category)
            .filter(id__gt=object.id)
            .order_by('id')
            .first()
        )

        context.update({'previous_object': previous_object,
                       'next_object': next_object})

        breadcrumbs = [
            {'name': ancestor.name, 'url': ancestor.get_absolute_url()}
            for ancestor in category.get_ancestors(include_self=True)
        ]

        breadcrumbs.append(
            {'name': object.name, 'url': object.get_absolute_url()})
        context['breadcrumbs'] = breadcrumbs

        context['main_title'] = object.name

        return context


    def render_to_response(self, context, **response_kwargs):
        """
        Renders the response based on the request type.

        Args:
            context (dict): The context for rendering the response.
            response_kwargs (dict): Additional keyword arguments for the response.

        Returns:
            HttpResponse: The rendered response.
        """
        if self.request.headers.get('HX-Request') == 'true':
            # Handle HTMX requests and return only the HTML content of the list portion
            if self.request.headers.get('source') == 'navBar':
                html = render_block_to_string(
                    'products/product.html', 'content', {**context, **global_context(self.request)})
                return HttpResponse(html)
            return render(self.request, 'products/partial/main-detail.html', context)
        else:
            # Handle regular requests and return the entire page's HTML
            return super().render_to_response(context, **response_kwargs)
