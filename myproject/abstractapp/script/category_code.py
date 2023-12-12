from products.models import Category


def bulk_generate_hierarchical_node_code(node, field_name='code', parent_code='', level=0, max_level=3):
    code_length_per_level = 2
    brand_code = getattr(node.get_root(), field_name, '')
    brand_code = brand_code if brand_code is not None else ''
    total_length = len(brand_code) + code_length_per_level * max_level

    current_code = ''  # 初始化current_code

    if level > 0:
        if not getattr(node, field_name):
            siblings_before = node.get_siblings(include_self=False).filter(id__lt=node.id).count()
            current_code = f'{siblings_before + 1:02d}'
            new_code = (brand_code + parent_code + current_code).ljust(total_length, '0')
            setattr(node, field_name, new_code)
            node.save()
        else:
            current_code = getattr(node, field_name)[-code_length_per_level:]  # 从已有的编码中提取当前层级的编码

    for child in node.get_children():
        child_level = level + 1
        child_parent_code = parent_code + current_code if level > 0 else ''
        bulk_generate_hierarchical_node_code(child, field_name, child_parent_code, child_level, max_level)


# 示例调用
for root_node in Category.objects.root_nodes():
    bulk_generate_hierarchical_node_code(root_node, level=0, max_level=3)
