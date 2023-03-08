from django.urls import path

from .views import HomeMenu, MenuItemDetail

urlpatterns = [
    path('', HomeMenu.as_view(), name="main_menu"),
    path('<slug:slug>/', MenuItemDetail.as_view(), name="menu_detail")
]