from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from hotels.models import Hotel
from hotels.forms import HotelCreateForm
from users.mixins import AdminAccess, ManagementAccess


class HotelListView(AdminAccess, ListView):
    model = Hotel
    template_name = 'hotels/hotel_list.html'
    context_object_name = 'hotels'
    ordering = ('name',)


class HotelCreateView(ManagementAccess, CreateView):
    model = Hotel
    template_name = 'hotels/hotel_create.html'
    form_class = HotelCreateForm

    def get_success_url(self):
        messages.success(self.request, "Hotel created successfully!")
        if self.request.user.user_type == 'admin':
            return reverse_lazy('hotels:hotel_list')
        else:
            return reverse_lazy('users:home')


class HotelUpdateView(ManagementAccess, UpdateView):
    model = Hotel
    template_name = 'hotels/hotel_update.html'
    form_class = HotelCreateForm

    def get_success_url(self):
        messages.success(self.request, "Hotel updated successfully!")
        if self.request.user.user_type == 'admin':
            return reverse_lazy('hotels:hotel_list')
        else:
            return reverse_lazy('users:home')


class HotelDeleteView(ManagementAccess, DeleteView):
    model = Hotel
    template_name = 'hotels/hotel_delete.html'
    context_object_name = 'data'

    def get_success_url(self):
        messages.success(self.request, "Hotel deleted successfully!")
        if self.request.user.user_type == 'admin':
            return reverse_lazy('hotels:hotel_list')
        else:
            return reverse_lazy('users:home')
