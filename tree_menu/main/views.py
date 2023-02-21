from django.views.generic import ListView
from .models import Menu, Item


class HomeMenu(ListView):
    model = Menu
    template_name = 'main/home_main.html'
    context_object_name = 'menu_list'
