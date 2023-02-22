from django.contrib import admin

from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "parrent", "parrent_id"]
    prepopulated_fields = {"slug": ("title",)}
