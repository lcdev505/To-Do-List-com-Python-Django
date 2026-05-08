from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('adicionar/', views.addTask, name="addTask"),
    path('editar/<int:pk>/', views.updateTask, name="updateTask"),
    path('apagar/<int:pk>/',views.deleteTask, name="deleteTask"),
    path('checkbox/<int:pk>/', views.checkboxTask, name="checkboxTask"),
]