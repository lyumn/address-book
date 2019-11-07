from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)