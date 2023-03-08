from django.views.generic import ListView, DetailView

from .models import MenuItem


class HomeMenu(ListView):
    model = MenuItem
    template_name = "main/home_main.html"
    context_object_name = "main_menu"

    def get_queryset(self):
        return MenuItem.objects.filter(nesting_level=1).first()


class MenuItemDetail(DetailView):
    model = MenuItem
    context_object_name = "main_menu"
    queryset = MenuItem.objects.select_related("parrent")
