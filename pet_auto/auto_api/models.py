from django.db import models


class Announcement(models.Model):
    """Объявление"""
    ad_id = models.SmallIntegerField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    photo = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    price_usd = models.SmallIntegerField()
    price_uah = models.SmallIntegerField()
    year = models.SmallIntegerField()
    race = models.SmallIntegerField()
    gearbox = models.CharField(max_length=256)
    drivename = models.CharField(max_length=256)
    vin = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f'{self.title} ID-{self.ad_id}'