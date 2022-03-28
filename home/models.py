from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='country_images',)
    details = models.TextField( null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    starting_prices = models.CharField(max_length=100, null=True, blank=True)
    flight = models.CharField(max_length=100, null=True, blank=True)
    pickup = models.CharField(max_length=100, null=True, blank=True)
    accomodation = models.CharField(max_length=100, null=True, blank=True)
    tour_cars = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name
    

class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    flight = models.BooleanField()
    accomodation = models.BooleanField()
    pick_up = models.BooleanField()
    tour_cars = models.BooleanField()

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{ self.first_name } { self.last_name }'
        else:
            return self.email
    
    