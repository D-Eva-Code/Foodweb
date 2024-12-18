from django.contrib import admin
from django.urls import path
from Food_app import views
from .views import ModelDetailView 


urlpatterns = [
    path('Menu',views.menu, name = "menu"),
    path('Item',views.item, name = "item"),
    # path('details/<item_id>',views.details, name = "details"),
    path('<int:pk>',ModelDetailView.as_view(), name = "details"),
    path('form', views.create, name= "create"),
    path('edit/<edit_id>',views.edit, name = "edit"),
    path('delete/<delete_id>',views.delete, name = "delete"),
]



