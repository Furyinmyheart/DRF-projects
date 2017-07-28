from rest_framework import viewsets
from .serializers import ChannelSerializer
from .models import Campaign
from .models import Channel

class ChannelViewSet(viewsets.ModelViewSet):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class CampaignViewSet(viewsets.ModelViewSet):

    queryset = Campaign.objects.all()