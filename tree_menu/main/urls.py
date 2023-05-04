from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('<slug:slug>/', index, name="index")
    # path('', HomeMenu.as_view(), name="main_menu"),
    # path('<slug:slug>/', MenuItemDetail.as_view(), name="menu_detail")
]