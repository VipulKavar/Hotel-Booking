from django.shortcuts import redirect
from django.contrib import messages
import datetime
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from bookings.models import Booking
from bookings.forms import BookingCreateForm
from users.mixins import ManagementAccess


class BookingListView(ManagementAccess, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'
    ordering = ('-booking_id',)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        if user.user_type == 'admin':
            return context
        else:
            context['bookings'] = Booking.objects.filter(hotel__manager=self.request.user)
            return context


class BookingCreateView(ManagementAccess, CreateView):
    model = Booking
    template_name = 'bookings/booking_create.html'
    form_class = BookingCreateForm

    def form_valid(self, form):
        # Validating Start and End Dates
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        today = datetime.datetime.now().date()
        if today < start_date < end_date:
            form.save()
            messages.success(self.request, "Booking Created Successfully!")
            return redirect(reverse('bookings:booking_list'))
        else:
            if today >= start_date:
                form.add_error(field='start_date', error='Start date must be greater than today.')
            elif end_date <= start_date:
                form.add_error(field='end_date', error='End date must be greater than start date.')
            return super(BookingCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('bookings:booking_list')


class BookingUpdateView(ManagementAccess, UpdateView):
    model = Booking
    template_name = 'bookings/booking_update.html'
    form_class = BookingCreateForm

    def form_valid(self, form):
        # Validating Start and End Dates
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        today = datetime.datetime.now().date()
        if today < start_date < end_date:
            form.save()
            return redirect(reverse('bookings:booking_list'))
        else:
            if today >= start_date:
                form.add_error(field='start_date', error='Start date must be greater than today.')
            elif end_date <= start_date:
                form.add_error(field='end_date', error='End date must be greater than start date.')
            return super(BookingUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('bookings:booking_list')


class BookingDeleteView(ManagementAccess, DeleteView):
    model = Booking
    template_name = 'bookings/booking_delete.html'
    context_object_name = 'data'

    def get_success_url(self):
        return reverse('bookings:booking_list')
