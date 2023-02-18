from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse

from hotels.models import Hotel


class AdminAccess(LoginRequiredMixin, UserPassesTestMixin):
    def get_test_func(self):
        """ Overriding test_func() of UserPassesTestMixin """
        user = self.request.user
        return True if user.is_authenticated and user.user_type == 'admin' else False

    def handle_no_permission(self):
        """ When permissions denied, This function will return according to it """
        user_test_result = self.get_test_func()
        if self.request.user.is_authenticated:
            if not user_test_result:
                return redirect(reverse('users:user_forbidden'))
            else:
                return super().handle_no_permission()
        else:
            return redirect(reverse('users:user_login'))


class ManagementAccess(LoginRequiredMixin, UserPassesTestMixin):
    def get_test_func(self):
        """ Overriding test_func() of UserPassesTestMixin """
        status = False

        user = self.request.user
        if user.is_authenticated:
            if user.user_type == 'admin':
                status = True

            elif user.user_type == 'manager':
                status = True
                pk = self.kwargs.get('pk', None)
                split_url = self.request.build_absolute_uri().split('/')

                # Manager can access only own hotel
                if pk and 'hotels' in split_url:
                    hotel_instance = Hotel.objects.get(pk=pk)
                    if user != hotel_instance.manager:
                        status = False
        return status

    def handle_no_permission(self):
        """ When permissions denied, This function will return according to it """
        user_test_result = self.get_test_func()
        if self.request.user.is_authenticated:
            if not user_test_result:
                return redirect(reverse('users:user_forbidden'))
            else:
                return super().handle_no_permission()
        else:
            return redirect(reverse('users:user_login'))
