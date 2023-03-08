from django.views.generic import ListView, DetailView

from .models import MenuItem, Menu


class HomeMenu(ListView):
    model = Menu
    template_name = "main/home_main.html"
    context_object_name = "main_menu"

    def get_queryset(self):
        return Menu.objects.select_related().all()


class MenuItemDetail(DetailView):
    model = MenuItem
    context_object_name = "main_menu"
    queryset = MenuItem.objects.select_related("parrent")
