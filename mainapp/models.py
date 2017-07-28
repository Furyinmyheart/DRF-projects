from django.db import models

class channel(models.Model):
    Name = models.CharField(max_length=32)
    Slug = models.CharField(max_length=32)
    BidTypes = models.TextField()

class campaign(models.Model):
    Name = models.CharField(max_length=32)
    Channel = models.ForeignKey(channel)
    Bid = models.FloatField()
    BidTypes = models.TextField()