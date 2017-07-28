from django.contrib import admin
from .models import Channel, Campaign


class ChannelModelAdmin(admin.ModelAdmin):
    list_display = [Campaign, 'Name', 'Slug', 'BidTypes']
    class Meta:
        model = Channel


class CampaignModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Bid']
    class Meta:
        model = Campaign

admin.site.register(Channel, ChannelModelAdmin)

admin.site.register(Campaign, CampaignModelAdmin)