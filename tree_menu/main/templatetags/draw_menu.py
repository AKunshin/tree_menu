from django import template
from django.shortcuts import get_object_or_404
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("inc/_root_menu.html", takes_context=True)
def draw_menu(context: dict(), menu_name: str):
    """
    A function for rendering menus.
    From the context dictionary we get the url requested by the user.
    Variable menu_name: this is the name of the menu that needs to be rendered.
    """
    request_url = context['request'].path.strip("/")
    menu_header = get_object_or_404(MenuItem, title=menu_name)
    active_branch = []
    active_item = None

    if not request_url == "":
    #Checking the home page
        try:
            active_item = get_object_or_404(MenuItem, slug=request_url)
            active_branch.append(active_item)
        except Exception as e:
            logger.error(f"Exception: {e}")

    def get_active_branch(object: MenuItem) -> list[object]:
        """
        Function for getting the active menu branch.
        Builds a list of all the objects parents up to the root
        """
        parent_menu_item = object.parrent
        if parent_menu_item:
            active_branch.append(parent_menu_item)
            get_active_branch(parent_menu_item)
        return active_branch

    if active_item:
        active_branch = get_active_branch(active_item)

    context = {
        "menu_header": menu_header,
        "active_item": active_item,
        "active_branch": active_branch,
    }

    return context
