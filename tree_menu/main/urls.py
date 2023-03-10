from django.urls import path

from .views import HomeMenu, MenuItemDetail

urlpatterns = [
    path('', HomeMenu.as_view(), name="main_menu"),
    path('<slug:menu_slug>/<slug:slug>/', MenuItemDetail.as_view(), name="menu_detail")
]