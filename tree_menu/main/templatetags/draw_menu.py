from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]
    root_menu_items = MenuItem.objects.filter(nesting_level=1)

    logger.debug(f"Сам item: {item}")


    # item.children = item.childs.all()
    # _branch = list(item)
    #Объявляем свойство childern - список дочерних пунктов

    # logger.debug(f"branch: {branch}")
    # logger.debug(f"item.children: {item.children}")
    _branch = []
    def get_upper_level_menu(object):
        """Builds a list of all the objects parents up to the root"""

        logger.debug(f"object in get_upper_level_menu: {object}")
        object.children = object.childs.all()
        _branch.append(object)
        logger.debug(f"branch: {_branch}")

        upp_level_menu_item = object.parrent
        logger.debug(f"upp_level_menu_item: {upp_level_menu_item}")
        if upp_level_menu_item:
            if upp_level_menu_item.nesting_level >= 1:

                upp_level_menu_item.children = upp_level_menu_item.childs.all()
                logger.debug(f"upp_level_menu_item.children: {upp_level_menu_item.children}")
                get_upper_level_menu(upp_level_menu_item)
        logger.debug(f"branch: {_branch}")
        return _branch

    def build_menu_tree(objects):
        """Builds a list of all menu objects"""
        _branch = get_upper_level_menu(item)
        logger.debug(f"_branch: {_branch}")
        root_item_for_item = _branch.pop()
        _branch.reverse()
        logger.debug(f"root_item_for_item: {root_item_for_item}")
        for root_item in root_menu_items:
            if root_item == root_item_for_item:
                root_item.children = root_item_for_item.childs.all()
                logger.debug(f"root_item.children: {root_item.children}")
        logger.debug(f"root_menu_items: {root_menu_items}")        
        return root_menu_items

    menu_list = build_menu_tree(root_menu_items)
    logger.debug(f"menu_list {menu_list}")

    for item in menu_list:
        try:
            logger.debug(f"item.children: {item.children}")
            for it1 in item.children:
                logger.debug(f"it1.children: {it1.children}")
        except:
            logger.debug(f"у {item} нет потомков")


    return {"menu_list": menu_list}
