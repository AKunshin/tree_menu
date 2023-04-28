from django.contrib import admin

from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "parrent", "nesting_level"]
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", "slug", "parrent", "nesting_level")
