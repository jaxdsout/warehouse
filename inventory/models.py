from django.db import models
from django.utils import timezone
import datetime

def upload_to(instance, filename):
    return 'items/{filename}'.format(filename=filename)

class Creator(models.Model):
    ROLES = [
        ('artist', 'Artist'),
        ('designer', 'Designer'),
        ('company', 'Company')
    ]
    role = models.CharField(max_length=8, choices=ROLES)
    name = models.CharField(max_length=150)
    about = models.TextField(max_length=1000)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Item (models.Model):
    CATEGORIES = [
        ('painting', 'Painting'),
        ('wallart', 'Wall Art'),
        ('prints', 'Prints'),
        ('objects', 'Objects'),
        ('goods', 'Goods')
    ]
    category = models.CharField(max_length=9, choices=CATEGORIES)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    materials_used = models.CharField(max_length=200)
    creation_period = models.CharField(max_length=200)
    dimensions = models.CharField(max_length=150)
    listing_start = models.DateField(blank=True)
    listing_end = models.DateField(blank=True)
    current_price = models.IntegerField(default=0)
    starting_price = models.IntegerField(default=1)
    image = models.ImageField(upload_to=upload_to, default='default.jpg', null=True, blank=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.title


class Bid (models.Model):
    amount = models.IntegerField(default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bids')
    time = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.item.current_price = self.amount
        self.item.save()

        super(Bid, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.amount} for {self.item}"
    

class Event (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    poster = models.ImageField(upload_to=upload_to, default='default.jpg', null=True, blank=True)
    time = models.DateTimeField(blank=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='events', null=True, blank=True)


    def __str__(self):
        return self.title
