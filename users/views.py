# users\views.py
import secrets

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages

from config.settings import EMAIL_HOST_USER
from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("diary:home")

    def form_valid(self, form):
        # Сохраняем пользователя без создания токена и отправки письма
        user = form.save()
        user.is_active = True  # Активируем пользователя сразу (можно оставить False, если нужно подтверждение)
        user.save()

        messages.success(self.request, "Вы успешно зарегистрированы. Теперь вы можете войти.")
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("diary:home")

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active:
            messages.error(self.request, "Ваш email не подтвержден. Пожалуйста, проверьте почту.")
            return HttpResponseRedirect(reverse_lazy("users:login"))  # Перенаправляем обратно на вход
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    template_name = "users/logout.html"
    next_page = reverse_lazy(
        "users:register"
    )  # Перенаправление на страницу регистрации после выхода


class PasswordResetView_(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'  # Шаблон для письма
    subject_template_name = 'users/password_reset_subject.txt'  # Тема письма
    success_url = reverse_lazy('users:password_reset_done')


class PasswordResetDoneView_(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView_(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

class PasswordResetCompleteView_(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'