from rest_framework import viewsets
import telegram
from django.conf import settings

from pet_auto.auto_api.models import Announcement

class BotViewSet(viewsets.GenericViewSet):
    """pass"""
    bot = telegram.Bot(token=f'{settings.TELEGRAM_API_KEY}')

    def send_message(ad_id):
        
        a = Announcement.objects.get(ad_id=ad_id)

        BotViewSet.bot.send_message(
            text=f'''Новое объявление {a.title}
год {a.year}, пробег {a.race}т.км коробка {a.gearbox}
цена {a.price_usd}$,   {a.price_uah} uah
фото {a.photo}
автор {a.author}    Описание:
{a.description}
vin {a.vin}
            ''', 
            chat_id=settings.CHAT_ID_1
            )

class NoticeViewSet(viewsets.GenericViewSet):
    """уведомления"""

    bot = telegram.Bot(token=f'{settings.TELEGRAM_API_KEY}')

    def hamster_notice():
        NoticeViewSet.bot.send_message(
            text=f'@{settings.USERNAME_2}, @{settings.USERNAME_3}, хомяк нуждается в проверке ', 
            chat_id=settings.CHAT_ID_2
            )

    def cats_fish_notice():
        NoticeViewSet.bot.send_message(
            text=f'@{settings.USERNAME_2}, @{settings.USERNAME_3}, Кто покормит котов и рыбок? + в чат', 
            chat_id=settings.CHAT_ID_2
            )

    def medicine_notice_s():
        NoticeViewSet.bot.send_message(
            text=f'@{settings.USERNAME_2}, @{settings.USERNAME_1}, время пить Сертралин', 
            chat_id=settings.CHAT_ID_2
            )

    def medicine_notice_p():
        NoticeViewSet.bot.send_message(
            text=f'@{settings.USERNAME_2}, @{settings.USERNAME_1}, время пить Прегабалин', 
            chat_id=settings.CHAT_ID_2
            )
