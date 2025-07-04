from django.urls import path, re_path
from .views import Home

app_name = "home"

urlpatterns = [
    path("", Home.home, name="home"),
]