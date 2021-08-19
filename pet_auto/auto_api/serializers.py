from rest_framework import serializers

from pet_auto.auto_api.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = (
            'ad_id', 'title', 'description', 'photo', 'author', 'price_usd',
            'price_uah', 'year', 'race', 'gearbox', 'vin', 
            )