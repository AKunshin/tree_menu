from django import template
from loguru import logger
from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("main/root_menu.html", takes_context=True)
def draw_menu(context: dict(), menu_name: MenuItem):
    menu = menu_name
    logger.debug(f"active_menu: {menu}")
    request_url = context['request'].path.strip("/")
    logger.debug(f"request_url: {request_url}")

    menu_header = MenuItem.objects.get(title=menu)
    branch = [menu_header]
    active_item = menu_header
    logger.debug(f"menu_header: {menu_header}")
    try:
        if request_url != "":
            active_item = MenuItem.objects.get(slug=request_url)
            logger.debug(f"active_item: {active_item}")
            branch.append(active_item)
    except Exception as e:
        logger.error(f"Exception: {e}")



    def get_active_branch(object: MenuItem) -> list[object]:
        """Builds a list of all the objects parents up to the root"""
        under_menu_item = object.parrent
        if under_menu_item:
            branch.append(under_menu_item)
            get_active_branch(under_menu_item)
        return branch
    
    
    active_branch = get_active_branch(active_item)
    logger.debug(f"active_branch: {active_branch}")

    context = {
        "menu_header": menu_header,
        "active_item": active_item,
        "active_branch": active_branch,
    }

    return context
