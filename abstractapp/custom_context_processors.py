from products.models import Category as ProductCategory  # 导入您的 Category 模型
from blog.models import Category as BlogCategory


def categories(request):
    # 获取所有的分类数据
    product_categories = ProductCategory.objects.all()
    # 查找根节点，假设根节点没有父节点
    product_root_categories = ProductCategory.objects.filter(level=1)

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
