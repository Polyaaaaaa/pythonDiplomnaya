from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from diary.forms import NoteForm
from diary.models import Note


# Create your views here.

class HomeView(ListView):
    model = Note
    template_name = "diary/home.html"
    context_object_name = "notes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NoteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "diary/note_form.html"
    success_url = reverse_lazy("diary:home")

    def test_func(self):
        return self.request.user.has_perm("diary.can_create_note")

    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем автора
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "diary/note_form.html"

    def test_func(self):
        return self.request.user.has_perm("diary.can_edit_note")

    def get_success_url(self):
        return reverse("diary:note_detail", args=[self.object.pk])


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = "diary/note_confirm_delete.html"
    success_url = reverse_lazy("diary:home")

    def test_func(self):
        return self.request.user.has_perm("diary.can_delete_note")

    def post(self, request, *args, **kwargs):
        if not self.test_func():
            return HttpResponseForbidden("У вас нет прав для удаления этой заметки.")
        return super().post(request, *args, **kwargs)


class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note
    template_name = "diary/note_detail.html"
    context_object_name = "note"

    def test_func(self):
        return self.request.user.has_perm("diary.view_all_note")


class NoteListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Note
    template_name = "diary/note_list.html"
    context_object_name = "notes"

    def test_func(self):
        return self.request.user.has_perm("diary.view_all_note")

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_delete"] = self.request.user.has_perm("diary.can_delete_note")
        return context

