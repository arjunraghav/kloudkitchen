from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, TemplateView, UpdateView, RedirectView
from django.urls import reverse_lazy
from .models import *
from .forms import *

User = get_user_model()


# Create your views here.

class CustomSignup(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'acnt/signup.html'
    success_url = reverse_lazy('acnt:login')
    context_object_name = 'form'
    success_message = "Your profile was created successfully"


class CustomLogin(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'acnt/login.html'
    success_url = reverse_lazy('core_app:home')
    context_object_name = 'form'


class CustomLogout(LogoutView):
    template_name = 'acnt/login.html'


class MyAccountViews(UpdateView):
    model = CustomerProfile
    template_name = 'acnt/account_page.html'
    form_class = CustomerProfileForm
    success_url = reverse_lazy('acnt:account')
    context_object_name = 'form'
    queryset = CustomerProfile.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    # def get_queryset(self):
    #     print(self.kwargs)
    #     user = User.objects.get(id=self.kwargs.get("pk"))
    #     return CustomerProfile.objects.get(user=user)

    # def get_object(self, queryset=None):
    #     print(self.kwargs)
    #     return self.request.user

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['text'] = 'this is returned from context'
    #     # context['form'] = Testimonial.get_latest_3_testimonial()
    #     print(self.kwargs)
    #     return context


class AddMoney(RedirectView):
    pass
