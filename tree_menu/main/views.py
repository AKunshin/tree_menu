from django.views.generic import ListView, DetailView, TemplateView
from .models import MenuItem


class HomeMenu(ListView):
    model = MenuItem
    template_name = "main/home_main.html"
    context_object_name = "main_menu"

    def get_queryset(self):
        return MenuItem.objects.filter(nesting_level=1).first()

# class HomeMenu(TemplateView):
#     template_name = 'main/home_main.html'


class MenuItemDetail(DetailView):
    model = MenuItem
    context_object_name = "main_menu"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

        # main_menu = []
        # menu_item = MenuItem.objects.get(slug=self.kwargs["slug"])
        # main_menu.append(menu_item)
        # while menu_item.parrent:
        #     menu_item = menu_item.parrent
        #     main_menu.append(menu_item)
        #     print(f"menu_item: {menu_item}")
        #     if menu_item.nesting_level == 1:
        #         root_parrent = menu_item
        #         print(f"root_parrent: {root_parrent}")
        # print(f"main_menu: {main_menu}")

        # main_menu = MenuItem.objects.filter(nesting_level=1)

        # context["main_menu"] = main_menu

        # return context
