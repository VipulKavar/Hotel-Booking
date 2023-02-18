from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

from users.models import User
from cities.models import City


class Hotel(models.Model):
    """ Hotel Model """

    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    rating = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    """ Hotel Features Model """

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    wifi = models.CharField(max_length=55, null=True)
    ac = models.CharField(max_length=55, null=True)
    bar = models.CharField(max_length=55, null=True)
    gym = models.CharField(max_length=55, null=True)

    def __str__(self):
        return f"{self.hotel.name}'s Features"


class HotelImage(models.Model):
    """ Hotel Image Model """

    # Dynamically Set Upload path, We set Dynamic Hotel name's Folder.
    def get_upload_to(self, filename):
        return f'images/{self.hotel.name}/{filename}'

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_to)

    def save(self, *args, **kwargs):
        """ if the image size is greater than 3MB then Auto compress it. """
        if self.image and self.image.size > 3000000:
            img = Image.open(self.image)
            output = BytesIO()
            img.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.image = InMemoryUploadedFile(output,
                                              'ImageField',
                                              f"{self.image.name.split('.')[0]}.jpeg",
                                              'image/jpeg',
                                              sys.getsizeof(self.image),
                                              None)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hotel.name}'s Image"
