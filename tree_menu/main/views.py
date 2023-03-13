from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Menu


class HomeMenu(ListView):
    model = Menu
    template_name = "main/home_main.html"
    context_object_name = "main_menu"

    def get_queryset(self):
        return Menu.objects.select_related().all()


def get_menu_tree(request, menu_slug ,item_slug):
    menu = get_object_or_404(Menu, slug=menu_slug)
    requested_item = get_object_or_404(menu.items, slug=item_slug)
    main_menu = Menu.objects.select_related().all()
    context = {
        "main_menu": main_menu,
        "requested_item": requested_item,
    }

    return render(request, "main/menuitem_detail.html", context=context)