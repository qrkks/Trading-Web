from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
from slugify import slugify
from typing import Any
from django.db import transaction, models
import os


def generate_slug(instance: Any, *args: Any, **kwargs: Any) -> None:
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


def generate_custom_order(instance: Any, *args: Any, **kwargs: Any) -> None:
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


SUPPORTED_FORMATS = ('jpeg', 'jpg', 'png', 'bmp', 'gif', 'webp')


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
            new_image_name = os.path.splitext(image_field.name)[0] + f'.{output_format.lower()}'
            image_field.save(new_image_name, ContentFile(output.read()), save=False)
