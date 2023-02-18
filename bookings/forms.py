from django import forms

from bookings.models import Booking


class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'number_of_person', 'customer', 'hotel']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'number_of_person': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'hotel': forms.Select(attrs={'class': 'form-control'}),
        }