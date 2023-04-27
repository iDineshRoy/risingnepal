from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import UserRegistrationForm, UserLoginForm
from .models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    template_name = "newpost.html"
    success_url = reverse_lazy("login_user")
    form_class = UserRegistrationForm

    def form_valid(self, form):
        return super().form_valid(form)


class UserLoginView(LoginView):
    model = CustomUser
    template_name = "login_user.html"
    redirect_field_name = reverse_lazy("list_student")
    success_url = "/"
    authentication_form = UserLoginForm


class UserLogoutView(LogoutView):
    redirect_field_name = reverse_lazy("home")
    template_name = "logout_user.html"
