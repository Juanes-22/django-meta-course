from django.urls import path

from . import views

urlpatterns = [
    path("/menu/<int:menu_id>", views.menu_by_id, "menu_by_id")
]
