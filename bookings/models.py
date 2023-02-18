from django.db import models
import datetime

from hotels.models import Hotel
from users.models import User


class Booking(models.Model):
    def auto_booking_id():
        date = datetime.datetime.now().strftime('%y%m%d%H%M%S%f')
        return date

    booking_id = models.CharField(max_length=255, default=auto_booking_id, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_person = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking_id} by {self.customer.username} in {self.hotel.name}"
