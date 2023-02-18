# urls.py
from django.urls import path
from cities import views

app_name = 'cities'
urlpatterns = [
    path('create/multiple/', views.CreateMultipleCitiesView.as_view(), name='city_create_multiple'),
    path('list/', views.CityListView.as_view(), name='city_list'),
    path('add/', views.CityCreateView.as_view(), name='city_create'),
    path('<int:pk>/update/', views.CityUpdateView.as_view(), name='city_update'),
    path('<int:pk>/delete/', views.CityDeleteView.as_view(), name='city_delete'),
]
