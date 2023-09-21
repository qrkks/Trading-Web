from products.models import Category as ProductCategory  # 导入您的 Category 模型


def categories(request):
    # 获取所有的分类数据
    product_categories = ProductCategory.objects.all()
    # 在视图中为每个节点添加一个额外的属性,node属性会自动通过categories传递到上下文
    for node in product_categories:
        node.extra_indent = node.level 
    # 查找根节点，假设根节点没有父节点
    product_root_categories = ProductCategory.objects.filter(parent__isnull=True)

    # 在上下文中返回 categories
    return {
        'product_categories': product_categories,
        'product_root_categories': product_root_categories
    }
