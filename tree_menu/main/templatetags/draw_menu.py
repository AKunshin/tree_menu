from django import template

from main.models import MenuItem

register = template.Library()

@register.inclusion_tag("main/menu_list.html")
def draw_menu(main_menu):
    main_menu = MenuItem.objects.all()
    return {"menu_list": main_menu}