from django import template

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/root_menu.html", takes_context=True)
def draw_menu(context, main_menu: MenuItem):
    active_item = context["main_menu"]
    main_items = MenuItem.objects.filter(nesting_level=1)
    branch = [active_item]

    def get_active_branch(object: MenuItem) -> list[object]:
        """Builds a list of all the objects parents up to the root"""
        under_menu_item = object.parrent
        if under_menu_item:
            branch.append(under_menu_item)
            get_active_branch(under_menu_item)
        return branch

    active_branch = get_active_branch(active_item)

    return {
        "main_items": main_items,
        "active_item": active_item,
        "active_branch": active_branch,
    }
