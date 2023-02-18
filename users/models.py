from io import BytesIO
import sys
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

from cities.models import City


# Create your models here.
class User(AbstractUser):
    user_type_choices = (
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("customer", "Customer"),
    )
    mobile_number = models.CharField(max_length=255)
    gender = models.CharField(choices=(('male', 'Male'), ('female', 'Female')), max_length=255, default='male')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    user_type = models.CharField(max_length=255, choices=user_type_choices)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='m_avatar3.jpg', upload_to='images/profile/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.image and self.image.size > 1000000:
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






