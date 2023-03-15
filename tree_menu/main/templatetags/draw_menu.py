from django import template

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]
    root_menu_items = MenuItem.objects.filter(nesting_level=1)

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
        #The submenu is built including the root parent element
        root_item_for_submenu = submenu.pop()
        #Returning the root parent from the list

        for root_item in root_menu_items:
            if root_item == root_item_for_submenu:
                submenu.reverse()
                root_item.children = submenu
        return root_menu_items


    return {"menu_list": build_menu_tree(root_menu_items)}
