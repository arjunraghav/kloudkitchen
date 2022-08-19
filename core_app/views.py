from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from acnt.models import Testimonial
from core_app.models import *
from core_app.forms import *


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


class ManageMyMenuVendorCuisineCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('acnt:login')
    context_object_name = 'context'
    model = Cuisine
    queryset = Cuisine.objects.all()
    form_class = CuisineForm
    template_name = 'core_app/manage_menu_page_cuisine.html'
    # template_name = 'components/testing_page.html'
    success_url = reverse_lazy('core_app:manage_menu_add')

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)

        # if self.request.POST:
        #     context['form'] = {
        #         'cuisine_form': CuisineForm(self.request.POST),
        #         'dish_cat_form': DishCatForm(self.request.POST),
        #     }
        # else:
        #     context['form'] = {
        #         'cuisine_form': CuisineForm(),
        #         'dish_cat_form': DishCatForm()
        #     }

        context["cuisine"] = Cuisine.objects.all()
        return context


class ManageMyMenuVendorCuisineListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('acnt:login')
    http_method_names = ['get', 'post']
    allow_empty = True
    context_object_name = 'cuisine'
    model = Cuisine
    paginate_by = 10
    queryset = Cuisine.objects.all().order_by('title')
    template_name = 'core_app/partials/load_cuisine.html'

    def get(self, request, *args, **kwargs):
        self.kwargs['search'] = request.GET['search']
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        print("in context", self.kwargs)
        data = super().get_context_data(**kwargs)
        if 'search' in self.kwargs:
            search_term = self.kwargs['search']
            data['cuisine'] = Cuisine.objects.filter(title__contains=search_term)
            return data
        data['cuisine'] = Cuisine.objects.all()
        return data


class ManageMyMenuVendorDishCatCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('acnt:login')
    context_object_name = 'context'
    model = DishCategory
    queryset = DishCategory.objects.all()
    form_class = DishCatForm
    template_name = 'core_app/manage_menu_page_dish_cat.html'
    success_url = reverse_lazy('core_app:manage_menu_add_dish_cat')

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context["dish_cat"] = DishCategory.objects.all()
        return context


class ManageMyMenuVendorDishCatListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('acnt:login')
    http_method_names = ['get', 'post']
    allow_empty = True
    context_object_name = 'dish_cat'
    model = DishCategory
    paginate_by = 10
    queryset = DishCategory.objects.all().order_by('title')
    template_name = 'core_app/partials/load_dish_cat.html'

    def get(self, request, *args, **kwargs):
        self.kwargs['search'] = request.GET['search']
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        print("in context", self.kwargs)
        data = super().get_context_data(**kwargs)
        if 'search' in self.kwargs:
            search_term = self.kwargs['search']
            dish_cat = DishCategory.objects.filter(title__contains=search_term)
            print(dish_cat)
            if not dish_cat:
                cuisine = Cuisine.objects.filter(title__contains=search_term)
                for item in cuisine:
                    print(item)
                    dish_cat = DishCategory.objects.filter(cuisine=item)
                print(dish_cat)
            data['dish_cat'] = dish_cat
            return data
        data['dish_cat'] = DishCategory.objects.all()
        return data


class ManageMyMenuVendorDishCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('acnt:login')
    context_object_name = 'context'
    model = Dish
    queryset = Dish.objects.all()
    form_class = DishForm
    template_name = 'core_app/manage_menu_page_dish.html'
    success_url = reverse_lazy('core_app:manage_menu_add_dish')

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context["dish"] = Dish.objects.all()
        return context


class ManageMyMenuVendorDishListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('acnt:login')
    http_method_names = ['get', 'post']
    allow_empty = True
    context_object_name = 'dish_cat'
    model = Dish
    paginate_by = 10
    queryset = Dish.objects.all().order_by('title')
    template_name = 'core_app/partials/load_dish.html'

    def get(self, request, *args, **kwargs):
        self.kwargs['search'] = request.GET['search']
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        print("in context", self.kwargs)
        data = super().get_context_data(**kwargs)
        if 'search' in self.kwargs:
            search_term = self.kwargs['search']
            dish = Dish.objects.filter(title__contains=search_term)
            print(dish)
            if not dish:
                dish = Dish.objects.filter(dish_category__title__contains=search_term)
                print("level 1", dish)
                if not dish:
                    cuisine = Cuisine.objects.filter(title__contains=search_term)
                    print("level 2", cuisine)
                    for item in cuisine:
                        print(item)
                        dish = Dish.objects.filter(dish_category__cuisine=item)
                        print("level 3", dish)
            data['dish'] = dish
            return data
        data['dish'] = Dish.objects.all()
        return data


class VendorMenuIdCreateView(CreateView):
    context_object_name = 'context'
    model = VendorMenuId
    queryset = VendorMenuId.objects.all()
    form_class = VendorMenuIdForm
    template_name = 'core_app/vendor_menu_id_page.html'
    success_url = reverse_lazy('core_app:manage_menu_create_menu_id')


class VendorMenuCreateView(CreateView):
    context_object_name = 'context'
    model = VendorMenu
    queryset = VendorMenu.objects.all()
    form_class = VendorMenuForm
    template_name = 'core_app/vendor_menu_page.html'
    success_url = reverse_lazy('core_app:manage_menu_create_menu')
#
# # testing new pattern
# class NewManageMyMenuTemplateView(TemplateView):
#     http_method_names = ['get', 'post']
#     template_name = 'core_app/manage_menu_page_testing.html'
#
#
# class NewManageMyMenyCreateView(CreateView):
#     http_method_names = ['get', 'post']
#     context_object_name = 'context'
#     model = Cuisine
#     queryset = Cuisine.objects.all()
#     form_class = CuisineForm
#     template_name = 'core_app/manage_menu_page_testing.html'
#     success_url = reverse_lazy('core_app:new_manage_menu_template')
#
#     def get_context_data(self, **kwargs):
#         print(kwargs)
#         context = super().get_context_data(**kwargs)
#         context["cuisine"] = Cuisine.objects.all()
#         return context
