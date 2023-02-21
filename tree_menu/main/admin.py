from django.contrib import admin
from .models import Menu, Item


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["menu", "title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


