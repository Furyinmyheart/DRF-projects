from django.db import models

class Channel(models.Model):
    Name = models.CharField(max_length=32)
    Slug = models.CharField(max_length=32)
    BidTypes = models.TextField()

class Campaign(models.Model):
    Name = models.CharField(max_length=32)
    Channel = models.ForeignKey(Channel)
    Bid = models.FloatField()
    BidTypes = models.TextField()