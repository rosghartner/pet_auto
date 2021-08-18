from django.contrib import admin
from pet_auto.auto_api import models


@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'ad_id', 'author', 'price_usd', 'vin', )