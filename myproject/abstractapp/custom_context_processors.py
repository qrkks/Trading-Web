from django.conf import settings
from django.db.models import Q

from products.models import Category as ProductCategory  # 导入您的 Category 模型
from blog.models import Category as BlogCategory
from form_handlers.forms import InquiryForm
from pages.models import ContactInformation, SocialMedia

def categories(request):
    # 获取所有的分类数据
    product_categories = ProductCategory.objects.all()
    # 查找根节点，假设根节点没有父节点
    product_root_categories = ProductCategory.objects.filter(Q(level=1)|Q(level=1))

    

    # 获取所有的分类数据
    blog_categories = BlogCategory.objects.all()
    # 查找根节点，假设根节点没有父节点
    blog_root_categories = BlogCategory.objects.filter(level=1)

    # 在上下文中返回 categories
    return {
        'product_categories': product_categories,
        'product_root_categories': product_root_categories,
        
        'blog_categories':blog_categories,
        'blog_root_categories':blog_root_categories,
    }

def inquiry_form(request):
    return {
        'inquiry_form':InquiryForm(),
    }

def contact(request):
    contacts = ContactInformation.objects.all().order_by('custom_order')
    contact_dict = {contact.name: contact for contact in contacts}
    return {'contact': contact_dict}

def social(request):
    return {}

# 传递debug变量
def settings_context(request):
    return {'debug': settings.DEBUG}

def global_context(request):
    """
    Generate the global context dictionary for the request.
    Args:
        request: The HTTP request object.
    Returns:
        A dictionary containing global context data.
    """
    # Generate the context dictionary by merging the results of various helper functions
    context = {
        **categories(request),
        **inquiry_form(request),
        **contact(request),
        **social(request),
        **settings_context(request),
    }
    return context

