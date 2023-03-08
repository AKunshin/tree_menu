from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "parrent", "nesting_level"]
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", "slug", "parrent", "menu")
