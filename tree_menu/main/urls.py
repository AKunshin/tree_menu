from django.urls import path

from .views import HomeMenu, get_menu_tree

urlpatterns = [
    path('', HomeMenu.as_view(), name="main_menu"),
    path('<slug:menu_slug>/<slug:item_slug>/', get_menu_tree, name="menu_detail")
]