from django.db import models

class Quote(models.Model):
    zip = models.IntegerField(max_length=5)
    bedrooms = models.IntegerField(max_length=2)
    bathrooms = models.IntegerField(max_length=2)
    hours = models.IntegerField(max_length=2)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
