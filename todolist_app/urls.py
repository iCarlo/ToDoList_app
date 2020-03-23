from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_do/', views.add_do, name='add_do'),
    path('delete_do/<int:items_id>', views.delete_do, name='delete_do'),
]
