from products.models import Category


def bulk_generate_hierarchical_node_code(node, field_name='code', parent_code='', level=0, max_level=5):
    """
    为 MPTT 模型的节点生成层级敏感且长度统一的编码，可选加上根节点的编码作为前缀。

    参数:
    node: 当前处理的 MPTT 模型节点。
    field_name: 需要自增的字段名称，默认为 'code'。
    parent_code: 父节点的编码。
    level: 当前节点的层级。
    max_level: 最大层级数（不包括根节点）。
    """
    code_length_per_level = 2  # 每个层级的编码长度
    brand_code = getattr(node.get_root(), field_name, '')  # 获取根节点的编码作为品牌编码
    # 当根节点没有编码时，将 brand_code 设为一个空字符串
    brand_code = brand_code if brand_code is not None else ''
    total_length = len(brand_code) + code_length_per_level * max_level  # 总编码长度

    if level > 0 and not getattr(node, field_name):
        # 计算编码
        siblings_before = node.get_siblings(include_self=False).filter(id__lt=node.id).count()
        current_code = f'{siblings_before + 1:02d}'
        new_code = (brand_code + parent_code + current_code).ljust(total_length, '0')

        setattr(node, field_name, new_code)
        node.save()

    # 递归处理子节点
    for child in node.get_children():
        child_level = level + 1
        child_parent_code = parent_code + current_code if level > 0 else ''
        bulk_generate_hierarchical_node_code(child, field_name, child_parent_code, child_level, max_level)

# 示例调用
for root_node in Category.objects.root_nodes():
    bulk_generate_hierarchical_node_code(root_node, level=0, max_level=4)
