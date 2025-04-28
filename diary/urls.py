# catalog/urls.py
from django.urls import path


app_name = "diary"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # URL для главной страницы
]