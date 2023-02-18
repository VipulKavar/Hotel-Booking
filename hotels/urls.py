from django.urls import path

from hotels import views


app_name = 'hotels'
urlpatterns = [
    path('list/', views.HotelListView.as_view(), name='hotel_list'),
    path('create/', views.HotelCreateView.as_view(), name='hotel_create'),
    path('update/<int:pk>/', views.HotelUpdateView.as_view(), name='hotel_update'),
    path('delete/<int:pk>/', views.HotelDeleteView.as_view(), name='hotel_delete'),
]
