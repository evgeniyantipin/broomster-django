from django.db import models


class Quote(models.Model):
    bedrooms_choices = (
        (1, '1 bedroom'),
        (2, '2 bedrooms'),
        (3, '3 bedrooms'),
        (4, '4 bedrooms'),
        (5, '5 bedrooms'),
        (6, '6 bedrooms'),
        (7, '7 bedrooms'),
        (8, '8 bedrooms'),
        (9, '9 bedrooms'),
        (10, '10 bedrooms'),
    )

    bathrooms_choices = (
        (1, '1 bathroom'),
        (2, '2 bathrooms'),
        (3, '3 bathrooms'),
        (4, '4 bathrooms'),
        (5, '5 bathrooms'),
        (6, '6 bathrooms'),
        (7, '7 bathrooms'),
        (8, '8 bathrooms'),
        (9, '9 bathrooms'),
        (10, '10 bathrooms'),
    )

    hours_choices = (
        (1, '1 hour'),
        (1.5, ' 1.5 hours'),
        (2, '2 hours'),
        (2.5, ' 2.5 hours'),
        (3, '3 hours'),
        (3.5, ' 3.5 hours'),
        (4, '4 hours'),
        (4.5, ' 4.5 hours'),
        (5, '5 hours'),
        (5.5, ' 5.5 hours'),
        (6, '6 hours'),
        (6.5, ' 6.5 hours'),
        (7, '7 hours'),
        (7.5, ' 7.5 hours'),
        (8, '8 hours'),
        (8.5, ' 8.5 hours'),
        (9, '9 hours'),
        (9.5, ' 9.5 hours'),
        (10, '10 hours'),
    )

    zip = models.IntegerField()
    bedrooms = models.IntegerField(choices=bedrooms_choices)
    bathrooms = models.IntegerField(choices=bathrooms_choices)
    hours = models.IntegerField(choices=hours_choices)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=50)
    apt = models.CharField(max_length=10, blank=True)  # this should be optional
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=10)
    extras = models.CharField(max_length=30)
