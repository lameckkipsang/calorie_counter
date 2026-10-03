from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracker, name='tracker'),
    path('delete/<int:item_id>/', views.delete_food, name='delete_food'),
]
