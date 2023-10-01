# middlewares.py

class BreadcrumbMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 获取请求的路径 (例如 '/home/about-us/')
        path = request.path

        # 根据斜杠分割路径，过滤掉空字符串
        parts = [part for part in path.split('/') if part]

        # 创建面包屑列表，初始时包含指向首页的链接
        breadcrumbs = [('Home', '/')]  # <<<<<< 这一行是新添加的 >>>>>>

        for i, part in enumerate(parts):
            # 创建每个面包屑的URL (例如 '/home/' 和 '/home/about-us/')
            url = '/' + '/'.join(parts[:i+1]) + '/'
            # 替换破折号和下划线为空格，并将部分转换为标题形式
            title = part.replace('-', ' ').replace('_', ' ').title()
            breadcrumbs.append((title, url))

        # 将面包屑添加到请求对象中，这样在视图和模板中都可以访问它们
        request.breadcrumbs = breadcrumbs

        response = self.get_response(request)
        return response

# from django.shortcuts import get_object_or_404
# from products.models import Category, Product

# class BreadcrumbsMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         category_path = request.resolver_match.kwargs.get('category_path', None)
#         slug = request.resolver_match.kwargs.get('slug', None)

#         breadcrumbs = [{'name': 'Home', 'url': '/'}]

#         if category_path:
#             slugs = category_path.split('/')
#             for i in range(1, len(slugs) + 1):
#                 partial_path = '/'.join(slugs[:i])
#                 category = get_object_or_404(Category, slug=slugs[i - 1])
#                 breadcrumbs.append({'name': category.name, 'url': f'/products/{partial_path}/'})

#         if slug:
#             product = get_object_or_404(Product, slug=slug)
#             breadcrumbs.append({'name': product.name, 'url': f'/products/{category_path}/{slug}/'})

#         request.breadcrumbs = breadcrumbs
#         response = self.get_response(request)

#         return response
