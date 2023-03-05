from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]

    logger.debug(f"Item: {item}")

    root_menu_items = MenuItem.objects.filter(nesting_level=1)



    def get_submenu(object) -> object:
        """Фуннкция для нахождения всех предков для объекта меню"""
        branch = [object.childs.all(), object]
        if object.parrent:
            submenu = object.parrent
            if submenu.nesting_level == 1:
                return branch
            else:
                branch.append(submenu)
                get_submenu(submenu)
        logger.debug(f"Get submenu: {branch}")
        return branch


    def build_menu_tree(objects) -> list:
        """Функция для построения списка всех объектов меню"""
        for root_item in root_menu_items:
            for second_item in root_item.childs.all():
                logger.debug(f"Second_item: {second_item}")
                if second_item in get_submenu(item):
                    root_item.children = get_submenu(item)
                    logger.debug(f"Root_item_children: {root_item.children}")
        logger.debug(f"Root_menu_items: {root_menu_items}")
        return root_menu_items


    return {"menu_list": build_menu_tree(root_menu_items)}
