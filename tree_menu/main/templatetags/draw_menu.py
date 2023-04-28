from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    active_item = context["main_menu"]
    logger.debug(f"active_item {active_item}")

    main_items = [MenuItem.objects.filter(nesting_level=1)]
    logger.debug(f"main_items {main_items}")

    def get_root_item(object):
        """Builds a list of all the objects parents up to the root"""
        logger.debug(f"object {object}")
        if object.parrent:
            parrent = object.parrent
            get_root_item(parrent)
        root_item = object
        logger.debug(f"root_item {root_item}")
        return root_item
    
    root_item = get_root_item(active_item)
    logger.debug(f"root_item: {root_item}")
    children = root_item.childs.all()
    logger.debug(f"children {children}")

    context = {
        "main_items": main_items,
        "root_item": root_item,
        "active_item": active_item,
        "children": children,
               }

    return context
