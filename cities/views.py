import pandas as pd
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView

from cities.forms import CreateMultipleCitiesForm
from cities.models import City
from cities.forms import CityForm
from users.mixins import AdminAccess


# Create your views here.
class CreateMultipleCitiesView(AdminAccess, FormView):
    form_class = CreateMultipleCitiesForm
    template_name = 'cities/create_multiple_cities.html'

    def post(self, request, *args, **kwargs):
        form = CreateMultipleCitiesForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('excel_file', None)
            df = pd.read_excel(file)
            City.objects.all().delete()
            for index, row in df.iterrows():
                data = City(name=row['city'], state=row['state'], country=row['country'])
                data.save()
            messages.success(request, "Multiple cities created successfully!")
            return redirect(reverse('cities:city_list'))


class CityListView(AdminAccess, ListView):
    template_name = 'cities/city_list.html'
    model = City
    context_object_name = 'cities'


class CityCreateView(AdminAccess, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/city_create.html'
    success_url = reverse_lazy('cities:city_list')


class CityUpdateView(AdminAccess, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/city_update.html'
    success_url = reverse_lazy('cities:city_list')


class CityDeleteView(AdminAccess, DeleteView):
    model = City
    template_name = 'cities/city_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('cities:city_list')
