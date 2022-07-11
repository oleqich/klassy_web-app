from turtle import position
from django.db import models

class ReserveModel(models.Model):
    NUMBER_CHOICES = (
        (1, '1'),(2, '2'),(3, '3'),(4, '4'),
        (5, '5'),(6, '6'),(7, '7'),(8, '8'),
        (9, '9'),(10, '10'),(11, '11'),(12, '12'),
    )

    TIME, BREAKFAST, LUNCH, DINNER = 'TIME', 'BREAKFAST', 'LUNCH', 'DINNER'
    TIME_CHOICES = (
        (TIME, 'Time'),
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )
    
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email', max_length=150)
    phone = models.CharField('Phone number', max_length=12)
    number_of_guests = models.IntegerField('Number of guests', choices=NUMBER_CHOICES, default=1)
    date = models.DateField('Date')
    time = models.CharField('Time', choices=TIME_CHOICES,  default=TIME, max_length=10)
    message = models.TextField('Message')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

def chef_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/chefs/chef_{0}/{1}'.format(instance.name, filename)

class ChefsModel(models.Model):
    name = models.CharField('Name and surname', max_length=100)
    position = models.CharField('Position', max_length=100)
    fb_link = models.URLField('Facebook link', max_length=200)
    tw_link = models.URLField('Twitter link', max_length=200)
    inst_link = models.URLField('Instagram link', max_length=200)
    image = models.ImageField(null=False, blank=False, upload_to=chef_directory_path, verbose_name='Image')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'
