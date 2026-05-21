from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('adicionar/', views.addTask, name="addTask"),
    path('editar/<int:pk>/', views.updateTask, name="updateTask"),
    path('apagar/<int:pk>/',views.deleteTask, name="deleteTask"),
    path('checkbox/<int:pk>/', views.checkboxTask, name="checkboxTask"),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/register/", views.register_view, name="register"),
    path("accounts/logout/", views.logout_view, name="logout"),
]