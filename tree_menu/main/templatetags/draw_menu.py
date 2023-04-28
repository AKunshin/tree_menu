from django import template
from loguru import logger

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/menu_list.html", takes_context=True)
def draw_menu(context, main_menu):
    item = context["main_menu"]

    logger.debug(f"Сам item:{item}")

    branch = list(item.childs.all())

    def get_upper_level_menu(object):
        """Builds a list of all the objects parents up to the root"""

        branch.append(object)
        logger.debug(f"object {object}")
        upp_level_menu_item = object.parrent
        logger.debug(f"upp_level_menu_item: {upp_level_menu_item}")
        if upp_level_menu_item:
            upp_level_menu_item.children = [object]
            get_upper_level_menu(upp_level_menu_item)
        logger.debug(f"branch: {branch}")
        return branch

    branch = get_upper_level_menu(item)
    branch.reverse()
    logger.debug(f"branch {branch}")

    return {"branch": branch}
