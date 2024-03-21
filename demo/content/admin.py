from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category, Tag, Article

class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Article)