from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/root_menu.html", takes_context=True)
def draw_menu(context, main_menu):
    active_item = context["main_menu"]
    logger.debug(f"active_item {active_item}")

    main_items = MenuItem.objects.filter(nesting_level=1)
    logger.debug(f"main_items {main_items}")
    branch=[active_item]


    def get_active_branch(object) -> list:
        """Builds a list of all the objects parents up to the root"""
        under_menu_item = object.parrent
        if under_menu_item:
            branch.append(under_menu_item)
            get_active_branch(under_menu_item)
        logger.debug(f"branch: {branch}")
        return branch
        
    active_branch = get_active_branch(active_item)
    root_item = active_branch[-1]
    logger.debug(f"root_item: {root_item}")


    return {
        "main_items": list(main_items),
        "active_item": active_item, 
        "active_branch": active_branch,
               }