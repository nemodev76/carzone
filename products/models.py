from django.db import models # type: ignore
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field # type: ignore
from multiselectfield import MultiSelectField # type: ignore
from .utils import sanitize_html

# Create your models here.
class Product(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2000, datetime.now().year+2):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=50)
    state = models.CharField(choices=state_choice, max_length=25)
    city = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    interior = models.CharField(max_length=25)
    year = models.IntegerField('year', choices=year_choice)
    condition = models.CharField(max_length=25)
    price = models.IntegerField()
    body_style = models.CharField(max_length=25)
    engine = models.CharField(max_length=25)
    drivetrain = models.CharField(max_length=25)
    transmission = models.CharField(max_length=25)
    miles = models.IntegerField()
    mileage = models.CharField(max_length=25)
    doors = models.CharField(choices=door_choices)
    passengers = models.IntegerField()
    vin_number = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=25)
    owners = models.IntegerField()
    is_featured = models.BooleanField()
    car_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_img1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_img2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_img3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_img4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=1000)
    description = CKEditor5Field(config_name='default')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.description = sanitize_html(self.description)
        super().save(*args, **kwargs)