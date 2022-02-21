from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from re import L, template
from . import forms, models


#메인 PAGE LISTVIEW로 수정해야함
def HomeView(request):
    return render(request, "core/home.html")


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")

def log_out(request):
    messages.info(request, "Success LogOut")
    logout(request)
    return redirect(reverse("core:home"))