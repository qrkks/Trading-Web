from django.db import transaction
from django.utils import timezone
import string
import random
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
from slugify import slugify
from typing import Any
from django.db import transaction, models
import os


def generate_slug_if_empty(instance: Any, *args: Any, **kwargs: Any) -> None:
    """
    Generate a slug for the given instance.

    Args:
        instance (Any): The instance for which the slug is generated.
        args (Any): Additional positional arguments.
        kwargs (Any): Additional keyword arguments.
    """
    # Check if instance already has a slug
    if not instance.slug:
        if hasattr(instance, 'name') and instance.name:
            base_slug = slugify(instance.name)
        elif hasattr(instance, 'title') and instance.title:
            base_slug = slugify(instance.title)
        # else:
        # # 处理没有 name 和 title 的情况
        # base_slug = 'default-slug'

        # Initialize slug with base slug
        slug = base_slug
        counter = 1
        # Get the model manager for the instance's class
        model_manager_instance = getattr(
            instance.__class__, instance._meta.default_manager_name or 'objects')
        # Check if a slug with the same base slug already exists
        while model_manager_instance.filter(slug=slug).exists():
            # Append counter to base slug to create a unique slug
            slug = f"{base_slug}-{counter}"
            counter += 1
        # Assign the generated slug to the instance
        instance.slug = slug


def generate_custom_order_if_empty(instance: Any, *args: Any, **kwargs: Any) -> None:
    """
    Generate a custom order for the given instance if it is a new record and has no specified custom order.
    Args:
        instance (Any): The instance for which to generate the custom order.
        args (Any): Additional positional arguments.
        kwargs (Any): Additional keyword arguments.
    """

    # Check if the instance is a new record and has no custom order specified
    if not instance.custom_order:

        # Start a database transaction
        with transaction.atomic():

            # Get the maximum custom order value from the instances of the same class
            max_custom_order = instance.__class__.objects.aggregate(
                models.Max('custom_order'))['custom_order__max'] or 0

            # Set the custom order of the instance to be one more than the maximum custom order value
            instance.custom_order = max_custom_order + 1


def generate_unique_filename(file_field, name_source, identifier_length=5):
    """
    Generates a unique filename for a file field based on a name source.

    Args:
        file_field: The file field to be renamed (can be any type of FileField or ImageField).
        name_source: A string representing the source of the name.
        identifier_length: Length of the random string to be appended. Defaults to 5.

    Returns:
        A unique filename string.
    """

    # Generate a random string of characters
    random_string = ''.join(random.choices(
        string.ascii_letters + string.digits, k=identifier_length))

    # Split the extension from the file name
    ext = file_field.name.split('.')[-1]

    # 获取当前的东八区时间
    now = timezone.now().astimezone(timezone.get_default_timezone())

    # Construct the unique file name
    unique_filename = f'{name_source}_{now.strftime("%Y%m%d%H%M")}_{random_string}.{ext}'

    return unique_filename


SUPPORTED_FORMATS = ('jpg', 'jpeg', 'png', 'gif', 'bmp',
                     'tif', 'tiff', 'webp', 'svg')


def resize_and_convert_image(image_field, width, output_format='webp', lossless=False, quality=80):
    """
    Resizes and converts an image.

    Parameters:
    - image_field: The image field to resize and convert.
    - width: The desired width of the resized image.
    - output_format: The desired output format of the converted image. Defaults to 'webp'.
    - lossless: A boolean indicating whether the converted image should be lossless. Defaults to True.
    - quality: The quality of the converted image, used only when output_format is 'webp' and lossless is False. Defaults to 80.

    Returns:
    None

    Raises:
    ValueError: If the output format is not supported.

    Description:
    This function takes an image field, a desired width, and optional parameters for output format, lossless compression, and quality. It resizes the image based on the given width and the aspect ratio of the original image. It then converts the resized image to the desired output format and saves it. If the output format is 'webp', the function can save the image with lossless or lossy compression based on the value of the lossless parameter. If the output format is not supported, a ValueError is raised.
    """
    # Check if the output format is supported
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported format: {output_format}. Supported formats are: {SUPPORTED_FORMATS}")

    # Ensure that the image file exists and has a valid extension
    if image_field and image_field.name.lower().endswith(SUPPORTED_FORMATS):
        # Open the image file
        with Image.open(image_field) as img:
            # Calculate the new height based on the given width and image's aspect ratio
            ratio = width / img.width
            new_height = int(img.height * ratio)

            # Resize the image and convert it to the desired format
            img_resized = img.resize((width, new_height))
            output = BytesIO()
            if output_format == 'webp':
                # Save the image in WEBP format with lossless or lossy compression
                if lossless:
                    img_resized.save(output, format='WEBP', lossless=True)
                else:
                    img_resized.save(output, format='WEBP', quality=quality)
            else:
                # Save the image in the desired output format
                img_resized.save(output, format=output_format.upper())
            output.seek(0)

            # Update the image field with the resized and converted image
            new_image_name = os.path.splitext(image_field.name)[
                0] + f'.{output_format.lower()}'
            image_field.save(new_image_name, ContentFile(
                output.read()), save=False)


def generate_hierarchical_node_code(node, field_name='code', max_level=3):
    """
    为 MPTT 模型的单个节点生成层级敏感且长度统一的编码，每个层级占用2位，总长8位。
    如果节点的code字段已存在，则不生成新的编码。

    参数:
    node: 当前处理的 MPTT 模型节点。
    field_name: 需要自增的字段名称，默认为 'code'。
    max_level: 最大层级数（不包括根节点）。
    """
    code_length_per_level = 2  # 每个层级的编码长度
    total_length = code_length_per_level * max_level  # 总编码长度

    # 仅当code字段不存在时，生成新的编码
    if not getattr(node, field_name):
        level = node.get_level()  # 获取当前节点的层级
        new_code = ''

        # 生成当前层级的编码
        siblings_before = node.get_siblings(
            include_self=False).filter(id__lt=node.id).count()
        current_level_code = f'{siblings_before + 1:02d}'

        if level == 1:
            # 对于根节点的直接子节点，直接使用当前层级的编码
            new_code = current_level_code.ljust(total_length, '0')
        elif level > 1:
            # 对于更深层级的节点，从父节点编码基础上生成编码
            parent_code = getattr(node.parent, field_name,
                                  '').ljust(total_length, '0')
            new_code = parent_code[:code_length_per_level *
                                   (level - 1)] + current_level_code
            # 保留当前层级之后的部分
            new_code += parent_code[code_length_per_level * level:]
        else:
            # 对于根节点，生成空编码
            new_code = ''.ljust(total_length, '0')

        setattr(node, field_name, new_code)
        node.save()


def generate_product_code(model_instance, related_field, prefix="CY", code_length=2, code_field="code"):
    """
    为模型实例生成编码。编码格式为 '{prefix}-{关联字段编码}-{自增编号}'

    参数:
    model_instance: 需要生成编码的模型实例。
    related_field: 关联字段的名称，用于获取关联模型的编码。
    prefix: 编码前缀，默认为 'CY'。
    code_length: 自增编号的长度，默认为 2。
    code_field: 编码字段的名称，默认为 'code'。
    """
    if getattr(model_instance, code_field):  # 如果编码已存在，则不进行更改
        return

    related_instance = getattr(model_instance, related_field)
    if not related_instance:
        # 如果没有关联实例，可以选择跳过编码生成或返回默认值
        return
    # 确保related_instance有一个code字段
    related_code = getattr(related_instance, code_field)

    # 获取相同关联字段下最后一个模型实例的编码
    last_instance = model_instance.__class__.objects.filter(
        **{related_field: related_instance}).order_by(code_field).last()

    new_seq_num = 1
    if last_instance and getattr(last_instance, code_field):
        try:
            last_seq_num = int(
                getattr(last_instance, code_field).split("-")[-1])
            new_seq_num = last_seq_num + 1
        except ValueError:
            # 处理可能的转换错误
            pass

    # 生成新的编码，自增编号部分不足code_length位用0补齐
    new_code = f'{prefix}-{related_code}-{new_seq_num:0{code_length}d}'
    setattr(model_instance, code_field, new_code)
