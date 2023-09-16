from products.models import Category  # 导入您的 Category 模型


def categories(request):
    # 获取所有的分类数据
    categories = Category.objects.all()
    # 在视图中为每个节点添加一个额外的属性,node属性会自动通过categories传递到上下文
    for node in categories:
        node.extra_indent = node.level 
    # 查找根节点，假设根节点没有父节点
    root_categories = Category.objects.filter(parent__isnull=True)

    # 在上下文中返回 categories
    return {
        'categories': categories,
        'root_categories': root_categories
    }
