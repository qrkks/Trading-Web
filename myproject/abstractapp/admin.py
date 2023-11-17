from django.contrib.admin import ModelAdmin
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField


class BaseModelAdmin(ModelAdmin):
    list_editable = ('is_active', 'is_featured')

    @property
    def list_display(self):
        return [
            field.name  # 获取字段的名称
            for field in self.model._meta.get_fields()  # 遍历模型的所有字段
            if not isinstance(field, (ForeignKey, ManyToManyField, OneToOneField))  # 条件：字段不是关系字段类型
        ]
    # model_name = self.model.__name__  # 这里获取模型的类名，即 "HomePage" 这里，self.model指向HomePage，因此self.model.__name__会返回字符串"HomePage"。

    @property
    def list_display_links(self):
        return [x for x in self.list_display if x not in self.list_editable]
