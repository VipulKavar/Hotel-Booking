from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, {self.state}"

