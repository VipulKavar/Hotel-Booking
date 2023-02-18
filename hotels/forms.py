from django import forms

from users.models import User, Profile
from hotels.models import Hotel, Feature, HotelImage


class HotelCreateForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'manager', 'contact_number', 'city', 'rating', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }