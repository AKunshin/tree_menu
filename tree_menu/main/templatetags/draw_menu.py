from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]

    logger.debug(f"Item: {item}")

    main_menu = MenuItem.objects.filter(nesting_level=1)

    # if item:
    # # item = MenuItem.objects.get(slug="item-2-1")
    #     print(f"Item.parrent {item.parrent}")

    def get_root_parrent(item) -> object:
        """Получение корневого родителя у объекта"""
        root_parrent = item.parrent
        if root_parrent.nesting_level > 1:
            root_parrent = get_root_parrent(root_parrent)
        return root_parrent

    # def get_children(parrent) -> list:
    #     """Функция для получения всех дочерних объектов"""
    #     children_list = []

    #     if parrent.childs:
    #         for child in parrent.childs.all():
    #             children_list.append(child)
    #             child.children = get_children(child)
    #     logger.debug(f"Chldren: {children_list}")
    #     return children_list
        # return get_children(parrent)
    
    _tree= []
    def get_children(parrent):
        children = [child for child in parrent.childs.all()]
        for child in children:
            _tree.append(child)
            if child.nesting_level != item.nesting_level:
                parrent.children = get_children(child)

        logger.debug(f"Tree: {_tree}")
        return _tree
        


    def build_menu_tree(objects) -> list:
        """Функция для построения списка всех объектов меню"""
        menu_list = []
        root_parrent = get_root_parrent(item)
        for menu_item in main_menu:
            if menu_item == root_parrent:
                menu_item.children = get_children(menu_item)
            menu_list.append(menu_item)
        
        logger.debug(f"Menu list: {menu_list}")
        return menu_list
    
    menu_list = build_menu_tree(main_menu)
    
    return {"menu_list": menu_list}
