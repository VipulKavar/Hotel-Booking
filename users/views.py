from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView

from users.models import User, Profile
from users.forms import UserCreateForm, UserRegistrationForm, UserUpdateForm, UserProfileForm, UserProfileUpdateForm
from users.mixins import AdminAccess, ManagementAccess


class HomeView(ManagementAccess, TemplateView):
    template_name = 'users/home.html'


class UserListView(AdminAccess, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserUpdateView(AdminAccess, UpdateView):
    model = User
    template_name = 'users/user_update.html'
    form_class = UserUpdateForm

    def get_context_data(self, **kwargs):
        """ Update user value, default will be updating user. """
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        return reverse_lazy('users:user_list')


class UserCreateView(AdminAccess, CreateView):
    model = User
    template_name = 'users/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        form.save()
        return redirect('users:user_list')


class UserDeleteView(AdminAccess, DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    context_object_name = 'data'

    def get_success_url(self):
        return reverse_lazy('users:user_list')


class UserProfileView(LoginRequiredMixin, UpdateView):

    def get(self, request, *args, **kwargs):
        data = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=request.user)
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)
        context = {
            'profile': profile,
            'data': data,
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'users/user_profile.html', context)

    def post(self, request, *args, **kwargs):
        u_form = UserProfileUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"{request.user.username.capitalize()}, Your profile has been updated.")
        return redirect(reverse_lazy('users:user_profile', kwargs=kwargs))


class ForbiddenView(TemplateView):
    template_name = 'users/user_403_forbidden.html'
