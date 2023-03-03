from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    main_menu = context["main_menu"]
    print(f"Main menu {main_menu}")
    item = MenuItem.objects.get(slug="item-1-1-1")
    print(f"Item.parrent {item.parrent}")

    parrent = main_menu.first()
    print(f"Parrent {parrent}")

    def get_root_parrent(item) -> object:
        """Получение корневого родителя у объекта"""
        root_parrent = item.parrent
        # print(f"root_parrent1 {root_parrent}")
        if root_parrent.nesting_level > 1:
            root_parrent = get_root_parrent(root_parrent)
            # print(f"root_parrent {root_parrent}")
        return root_parrent

    def get_children(parrent) -> list:
        """Функция для получения всех дочерних объектов"""
        children_list = []

        if parrent.childs:
            for child in parrent.childs.all():
                children_list.append(child)
                child.children = get_children(child)
            print(f"child list {children_list}")

        return children_list

    def build_menu_tree(objects) -> list:
        """Функция для построения списка всех объектов меню"""
        menu_list = []
        root_parrent = get_root_parrent(item)
        logger.debug(f"root_parrent {root_parrent}")
        for menu_item in main_menu:
            if menu_item == root_parrent:
                logger.debug(f"Menu_item {menu_item}")
                menu_item.children = get_children(menu_item)
            menu_list.append(menu_item)
            logger.debug(f"Menu list: {menu_list}")
        
        return menu_list
    
    menu_list = build_menu_tree(main_menu)
    
    return {"menu_list": menu_list}
