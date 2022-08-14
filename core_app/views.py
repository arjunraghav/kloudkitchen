from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from acnt.models import Testimonial


# Create your views here.

class IndexView(TemplateView):
    template_name = 'core_app/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is returned from context'
        context['testimonial'] = Testimonial.get_latest_3_testimonial()
        return context


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core_app/home_page.html'
    login_url = reverse_lazy('acnt:login')
    permission_denied_message = 'You are not allowed to access this page contact your admin'


class AboutView(TemplateView):
    template_name = 'core_app/aboutus_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is returned from context'
        context['testimonial'] = Testimonial.get_latest_3_testimonial()
        return context


class QuickMenuView(TemplateView):
    template_name = 'core_app/quick_menu_page.html'


class ManageMyMenuVendor(TemplateView):
    template_name = 'core_app/quick_menu_page.html'
