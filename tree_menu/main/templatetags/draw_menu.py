from django import template
from loguru import logger

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    menu_list = context["main_menu"]

    logger.debug(f"menu_list: {menu_list}")

    item = context.get("requested_item")

    if not item:
        context = {"menu_list": menu_list }
        return context
    else:
        logger.debug(f"Item: {item}")
        requested_menu = item.menu
        logger.debug(f"requested_menu: {requested_menu}")
        
        # root_menu_items = []
        root_menu_items = requested_menu.items.all().filter(nesting_level=1)
        logger.debug(f"root_menu_items: {root_menu_items}")

        
        branch = [children for children in item.childs.all()]
        branch.append(item)

        def get_submenu(object) -> list:
            """Builds a list of all the objects parents up to the root"""
            submenu_item = object.parrent
            if submenu_item:
                if submenu_item.nesting_level >= 1:
                    branch.append(submenu_item)
                    get_submenu(submenu_item)
            return branch

        def build_menu_tree(objects) -> list:
            """Builds a list of all menu objects"""
            submenu = get_submenu(item)
            root_item_for_submenu = submenu.pop()
            for root_item in root_menu_items:
                logger.debug(f"root_item: {root_item}")
                if root_item == root_item_for_submenu:
                    submenu.reverse()
                    root_item.children = submenu
            return root_menu_items

        menu_tree = build_menu_tree(root_menu_items)

        logger.debug(f"menu_tree: {menu_tree}")
    

    context = {"menu_list": menu_list, "menu_tree": menu_tree }
    return context
