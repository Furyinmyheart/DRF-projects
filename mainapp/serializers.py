from .models import Channel
from .models import Campaign
from rest_framework import serializers


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('Name', 'Slug', 'BidTypes')

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ('Name', 'Channel', 'Bid', 'BidTypes')