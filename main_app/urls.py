from django.urls import path,include, re_path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView





urlpatterns = [
    path('', views.index, name="index"),
]






