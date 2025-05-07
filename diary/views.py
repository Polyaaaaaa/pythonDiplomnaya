from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from diary.forms import NoteForm
from diary.models import Note


class HomeView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'diary/home.html'
    context_object_name = 'notes'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Note.objects.filter(user=self.request.user)
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Мои заметки"
        context['query'] = self.request.GET.get('q', '')
        return context


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "diary/note_form.html"
    success_url = reverse_lazy("diary:home")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Сохраняем автора
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "diary/note_form.html"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("diary:note_detail", args=[self.object.pk])


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "diary/note_confirm_delete.html"
    success_url = reverse_lazy("diary:home")

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "diary/note_detail.html"
    context_object_name = "note"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "diary/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_delete"] = self.request.user.has_perm("diary.can_delete_note")
        return context
