from django import template
from django.shortcuts import get_object_or_404
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/root_menu.html", takes_context=True)
def draw_menu(context: dict(), menu_name: MenuItem):
    menu = menu_name
    request_url = context['request'].path.strip("/")

    menu_header = get_object_or_404(MenuItem, title=menu)
    branch = [menu_header]
    active_item = menu_header
    try:
        active_item = get_object_or_404(MenuItem, slug=request_url)
        branch.append(active_item)
    except Exception as e:
        logger.error(f"Exception: {e}")

    def get_active_branch(object: MenuItem) -> list[object]:
        """Builds a list of all the objects parents up to the root"""
        under_menu_item = object.parrent
        if under_menu_item:
            branch.append(under_menu_item)
            get_active_branch(under_menu_item)
        return branch

    active_branch = get_active_branch(active_item)

    context = {
        "menu_header": menu_header,
        "active_item": active_item,
        "active_branch": active_branch,
    }

    return context
