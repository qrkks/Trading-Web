from products.models import Product
from abstractapp.func import generate_product_code


def batch_generate_codes(ModelClass, related_field):
    """
    批量为指定模型类的实例生成编码。

    参数:
    ModelClass: 需要处理的模型类。
    related_field: 关联字段的名称。
    """
    instances_without_code = ModelClass.objects.filter(code__isnull=True)
    for instance in instances_without_code:
        generate_product_code(instance, related_field)
        instance.save()


# 示例使用
# 在 Django shell 中运行
batch_generate_codes(Product, 'code')
