from django.urls import path
from .views import Home

app_name = "home"

urlpatterns = [
    path("home/", Home.home, name="home"),
]