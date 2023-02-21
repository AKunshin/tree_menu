from django.urls import path

from .views import HomeMenu

urlpatterns = [
    path('', HomeMenu.as_view(), name="main_menu"),
    path('menu/<slug:slug>/', HomeMenu.as_view(), name="menu_detail")
]