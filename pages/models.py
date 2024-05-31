from django.db import models # type: ignore

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=255)
    x_link = models.URLField(max_length=255)
    google_plus_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
    