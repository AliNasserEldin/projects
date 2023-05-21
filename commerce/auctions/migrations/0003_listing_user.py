# Generated by Django 4.2 on 2023-05-02 19:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ManyToManyField(related_name='creates', to=settings.AUTH_USER_MODEL),
        ),
    ]
