from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]
    root_menu_items = MenuItem.objects.filter(nesting_level=1)

    branch = [item.childs.all(), item]

    def get_submenu(object) -> list:
        """Функция для нахождения всех предков для объекта меню"""
        if object.parrent:
            submenu = object.parrent
            if submenu.nesting_level >= 1:
                branch.append(submenu)
                get_submenu(submenu)
        return branch

    def build_menu_tree(objects) -> list:
        """Функция для построения списка всех объектов меню"""
        for root_item in root_menu_items:
            submenu = get_submenu(item)
            logger.debug(f"item: {item}")
            logger.debug(f"root_item: {root_item}")
            logger.debug(f"get submenu item: {submenu}")
            if root_item == submenu[-1]:
                root_item.children = submenu
                logger.debug(f"Root_item_children: {root_item.children}")
                return root_menu_items
        logger.debug(f"Root_menu_items: {root_menu_items}")
        return root_menu_items

    return {"menu_list": build_menu_tree(root_menu_items)}
