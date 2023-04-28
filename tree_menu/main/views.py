from django.views.generic import ListView, DetailView

from .models import MenuItem


class HomeMenu(ListView):
    model = MenuItem
    template_name = "main/menuitem_detail.html"
    context_object_name = "root_menu"

    def get_queryset(self):
        return MenuItem.objects.filter(nesting_level=1)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_menu"] = MenuItem.objects.filter(nesting_level=1).first()
        return context


class MenuItemDetail(DetailView):
    model = MenuItem
    context_object_name = "main_menu"
    queryset = MenuItem.objects.select_related("parrent")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["root_menu"] = MenuItem.objects.filter(nesting_level=1)
        return context
