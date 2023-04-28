from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]
    root_menu_items = MenuItem.objects.filter(nesting_level=1)

    # Debug all objects
    all_objects = MenuItem.objects.all()
    for object in all_objects:
        object.has_chosen = None
        object.save()
        logger.debug(f"object :{object} object has chosen {object.has_chosen}")

    logger.debug(f"Сам item:{item} chosen: {item.has_chosen}")

    branch = []

    def get_upper_level_menu(object):
        """Builds a list of all the objects parents up to the root"""

        logger.debug(
            f"object in get_upper_level_menu: {object} has_chosen: {object.has_chosen}")
        object.has_chosen = True
        object.save()
        object.children = list(object.childs.all())
        branch.append(object)
        logger.debug(f"branch: {branch}")

        upp_level_menu_item = object.parrent
        logger.debug(f"upp_level_menu_item: {upp_level_menu_item}")
        if upp_level_menu_item:
            if upp_level_menu_item.nesting_level >= 1:

                upp_level_menu_item.has_chosen = True
                upp_level_menu_item.save()
                logger.debug(
                    f"upp_level_menu_item has been chosen: {upp_level_menu_item.has_chosen}")
                get_upper_level_menu(upp_level_menu_item)
        logger.debug(f"branch: {branch}")
        return branch

    def build_menu_tree(objects):
        """Builds a list of all menu objects"""
        _branch = get_upper_level_menu(item)
        logger.debug(f"_branch: {_branch}")
        root_item_for_item = _branch.pop()
        _branch.reverse()
        logger.debug(f"root_item_for_item: {root_item_for_item}")
        for root_item in root_menu_items:
            if root_item == root_item_for_item:
                root_item.has_chosen = True
                logger.debug(
                    f"root_item has been chosen: {root_item.has_chosen}")
        logger.debug(f"root_menu_items: {root_menu_items}")
        return root_menu_items

    menu_list = build_menu_tree(root_menu_items)
    logger.debug(f"menu_list {menu_list}")

    for object in all_objects:
        logger.debug(f"object :{object} object has chosen {object.has_chosen}")

    return {"menu_list": menu_list}
