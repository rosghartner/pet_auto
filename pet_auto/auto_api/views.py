import requests
from rest_framework import viewsets
from django.conf import settings

from pet_auto.auto_api.models import Announcement
from pet_auto.tbot.views import BotViewSet
from pet_auto.auto_api.serializers import AnnouncementSerializer


class AutoSearchViewSet(viewsets.GenericViewSet):
    """searching auto"""
    queryset = Announcement.objects.all
    serializer_class = AnnouncementSerializer

    def search():
        #Audi 100, 2.8 1992<i<2005, quattro, sedan
        r = requests.get(f'https://developers.ria.com/auto/search?api_key={settings.AUTORIA_API_KEY}&marka_id[0]=6&model_id[0]=39&s_yers[0]=1992&po_yers[0]=2005&engineVolumeFrom=2.8&drive_type[0]=1&bodystyle[0]=3')
        data = r.json()
        result = data.get('result')
        AutoSearchViewSet.comparsion(result)
        return data

    def comparsion(result):
        search_result = result.get('search_result')
        ids = search_result.get('ids')
        for i in ids:
            if Announcement.objects.filter(ad_id = i).exists():
                pass
            else:
                AutoSearchViewSet.create(i)

    def create(post_id):
        r = requests.get(f'https://developers.ria.com/auto/info?api_key={settings.AUTORIA_API_KEY}&auto_id={post_id}')
        data = r.json()
        auto_Data = data.get('autoData')
        photo_data = data.get('photoData')
        photo_all = photo_data.get('all')

        title = data.get('title')
        description = auto_Data.get('description')
        photo = f'https://cdn2.riastatic.com/photosnew/auto/photo/audi_100__{photo_all[0]}f.jpg'
        author = data.get('userId')
        price_usd = data.get('USD')
        price_uah =  data.get('UAH')
        year = auto_Data.get('year')
        race = auto_Data.get('raceInt')
        gearbox = auto_Data.get('gearboxName')
        vin = data.get('VIN')

        Announcement.objects.create(
            ad_id = post_id,
            title = title,
            description = description,
            photo = photo,
            author = author,
            price_usd = price_usd,
            price_uah = price_uah,
            year = year,
            race = race,
            gearbox = gearbox,
            vin = vin
        )
        BotViewSet.send_message(post_id)
        return Announcement
