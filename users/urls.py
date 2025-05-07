from django.urls import path

from diary.views import HomeView
from users.views import RegisterView, CustomLoginView, CustomLogoutView, PasswordResetView_, PasswordResetDoneView_, \
    PasswordResetConfirmView_, PasswordResetCompleteView_

app_name = "users"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(next_page="diary:home"), name="logout"),

    # Восстановление пароля
    path('password-reset/', PasswordResetView_.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView_.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView_.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView_.as_view(), name='password_reset_complete'),
]
