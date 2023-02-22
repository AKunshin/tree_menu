from django.views.generic import ListView, DetailView
from .models import MenuItem


class HomeMenu(ListView):
    model = MenuItem
    template_name = 'main/home_main.html'
    context_object_name = 'menu_list'


class MenuItemDetail(DetailView):
    model = MenuItem
    context_object_name = "menu_item"
