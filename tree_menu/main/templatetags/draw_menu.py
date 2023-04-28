from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]
    root_menu_items = MenuItem.objects.filter(nesting_level=1)

    branch = list(item.childs.all())

    logger.debug(f"branch: {branch}")

    branch.append(item)

    def get_submenu(object) -> list:
        """Builds a list of all the objects parents up to the root"""
        under_menu_item = object.parrent
        if under_menu_item:
            # if under_menu_item.nesting_level >= 1:
            branch.append(under_menu_item)
            get_submenu(under_menu_item)
        logger.debug(f"branch: {branch}")
        return branch

    def build_menu_tree(objects) -> list:
        """Builds a list of all menu objects"""
        submenu = get_submenu(item)
        #The submenu is built including the root parent element
        root_item_for_submenu = submenu.pop()
        #Returning the root parent from the list

        for root_item in root_menu_items:
            if root_item == root_item_for_submenu:
                submenu.reverse()
                root_item.children = submenu
        logger.debug(f"root_menu_items: {root_menu_items}")
        return root_menu_items

    menu_list = build_menu_tree(root_menu_items)
    return {"menu_list": menu_list}
