from django.db import models

class Cliente(models.Model):
    type = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    name_title = models.CharField(max_length=2)
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=100)
    location_region = models.CharField(max_length=30)
    location_street = models.CharField(max_length=100)
    location_city = models.CharField(max_length=30)
    location_state = models.CharField(max_length=30)
    location_postcode = models.CharField(max_length=30)
    location_coordinates_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_coordinates_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_timezone_offset = models.CharField(max_length=30)
    location_timezone_description = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    registered = models.CharField(max_length=50)
    picture_large = models.CharField(max_length=100)
    picture_medium = models.CharField(max_length=100)
    picture_thumbnail = models.CharField(max_length=100)
    nationality = models.CharField(max_length=2)
    telephone_numbers = models.CharField(max_length=20)
    mobile_numbers = models.CharField(max_length=20)

    def __str__(self):
        return self.name_first