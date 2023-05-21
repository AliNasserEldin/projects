from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing' , related_name='watches')

class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length=1000)

class Bid(models.Model):
    cash = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Listing(models.Model):
    AUCTION_CATEGORIES = (
    ('ART', 'Art'),
    ('BIKES', 'Bikes'),
    ('CARS', 'Cars'),
    ('CLOTHES', 'Clothes'),
    ('COMPUTERS', 'Computers'),
    ('ELECTRONICS', 'Electronics'),
    ('FURNITURE', 'Furniture'),
    ('HOME & GARDEN', 'Home & Garden'),
    ('JEWELRY', 'Jewelry'),
    ('MUSIC', 'Music'),
    ('OFFICE & SCHOOL SUPPLIES', 'Office & School Supplies'),
    ('SPORTS & OUTDOORS', 'Sports & Outdoors'),
    ('TOYS & GAMES', 'Toys & Games'),
    ('TRAVEL', 'Travel'),
    ('OTHER', 'Other'),
    )
    starting = models.IntegerField(blank = False, null=False)
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 1250)
    image = models.CharField(blank=True,max_length = 100)
    bids = models.ManyToManyField(Bid, related_name = "bids", blank=True)
    price = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User  , on_delete = models.CASCADE)
    winner = models.ForeignKey(User,related_name='winner', on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)
    comments = models.ManyToManyField(Comment, related_name='comments')
    category = models.CharField(max_length=25,choices=AUCTION_CATEGORIES,default='OTHER')