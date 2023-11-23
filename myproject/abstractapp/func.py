from slugify import slugify
from typing import Any
from django.db import transaction, models


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
        # Generate base slug from instance name
        base_slug = slugify(instance.name)
        # Initialize slug with base slug
        slug = base_slug
        counter = 1
        # Get the model manager for the instance's class
        model_manager_instance = getattr(instance.__class__, instance._meta.default_manager_name or 'objects')
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
            max_custom_order = instance.__class__.objects.aggregate(models.Max('custom_order'))['custom_order__max'] or 0
            
            # Set the custom order of the instance to be one more than the maximum custom order value
            instance.custom_order = max_custom_order + 1
            