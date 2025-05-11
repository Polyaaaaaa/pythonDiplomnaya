# catalog/urls.py
from django.urls import path

from .views import (
    NoteCreateView,
    NoteListView,
    NoteDetailView,
    NoteUpdateView,
    NoteDeleteView,
    HomeView,
)

app_name = "diary"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # URL для главной страницы
    path("create/", NoteCreateView.as_view(), name="note_create"),
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("<int:pk>/edit/", NoteUpdateView.as_view(), name="note_update"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
]
