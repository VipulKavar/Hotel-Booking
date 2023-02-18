from django.urls import path

from bookings import views


app_name = 'bookings'
urlpatterns = [
    path('list/', views.BookingListView.as_view(), name='booking_list'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('update/<int:pk>/', views.BookingUpdateView.as_view(), name='booking_update'),
    path('delete/<int:pk>/', views.BookingDeleteView.as_view(), name='booking_delete'),
]
