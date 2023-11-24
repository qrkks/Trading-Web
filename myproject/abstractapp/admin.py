from django.contrib.admin import ModelAdmin
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField


class BaseModelAdmin(ModelAdmin):
    list_editable = ('is_active', 'is_featured')


    @property
    def list_display(self):
        """
        Returns a list of field names for displaying in the admin list view.

        Only fields that are not relationship fields are included in the list.
        """
        return [
            field.name  # Get the name of the field
            for field in self.model._meta.get_fields()  # Loop through all fields of the model
            if not isinstance(field, (ForeignKey, ManyToManyField, OneToOneField))  # Condition: Field is not a relationship field type
        ]
    # model_name = self.model.__name__  # 这里获取模型的类名，即 "HomePage" 这里，self.model指向HomePage，因此self.model.__name__会返回字符串"HomePage"。

@property
def list_display_links(self):
    """
    Returns a list of display links for the model admin.

    These links are obtained from the `list_display` attribute,
    excluding any fields that are also present in `list_editable`.

    Returns:
        list: A list of display links for the model admin.
    """

    # Create a set of fields that can be edited in the list view
    list_editable_set = set(self.list_editable)

    # Iterate over the fields in the `list_display` attribute
    # and filter out the fields that are also present in `list_editable`
    display_links = [field for field in self.list_display if field not in list_editable_set]

    # Return the filtered list of display links
    return display_links
