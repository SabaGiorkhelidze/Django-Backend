from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Menu, Block
# SortableInlineAdminMixin


class BlockInline(admin.TabularInline):
    model = Block.articles.through
    extra = 1


@admin.register(Menu)
class MenuAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('name', 'link', 'is_external', 'category', 'is_active')
    list_editable = ('is_active',)


@admin.register(Block)
class BlockAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [BlockInline]
    list_display = ('title', 'block_style', 'position', 'row', 'show_title')
    list_editable = ('show_title',)

