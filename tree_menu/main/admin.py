from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "parrent"]
    prepopulated_fields = {"slug": ("title",)}
