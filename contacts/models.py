
from django.db import models # type: ignore
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    product_id = models.IntegerField()
    customer_need = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField(blank=True)
    user_id = models.IntegerField()
    date_created = models.DateTimeField(blank=True, default=datetime.now())

def __str__(self):
    return self.email