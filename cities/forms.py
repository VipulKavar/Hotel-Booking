from django import forms

from cities.models import City


class CreateMultipleCitiesForm(forms.Form):
    file = forms.FileInput()


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'state', 'country',)
