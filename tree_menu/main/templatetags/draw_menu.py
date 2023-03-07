from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]
    root_menu_items = MenuItem.objects.filter(nesting_level=1)

    branch = [item.childs.all(), item]
    logger.info(f"branch: {branch}")

    def get_submenu(object) -> list:
        """Builds a list of all the objects parents up to the root"""
        if object.parrent:
            submenu = object.parrent
            if submenu.nesting_level >= 1:
                branch.append(submenu)
                get_submenu(submenu)
        return branch

    def build_menu_tree(objects) -> list:
        """Builds a list of all menu objects"""
        submenu = get_submenu(item)
        root_item_for_submenu = submenu.pop()
        for root_item in root_menu_items:
            if root_item == root_item_for_submenu:
                submenu.reverse()
                root_item.children = submenu
                logger.debug(f"Root_item_children: {root_item.children}")
                return root_menu_items
        logger.debug(f"Root_menu_items: {root_menu_items}")
        return root_menu_items

    return {"menu_list": build_menu_tree(root_menu_items)}
