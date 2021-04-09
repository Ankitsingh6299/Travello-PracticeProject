from django.urls import path

from . import views

urlpatterns = [
    path("registeration", views.registeration, name="registeration"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    ]
