from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.

class HomeView(ListView):
    model = Note
    template_name = "mailing_management/home.html"
    context_object_name = "clients"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

