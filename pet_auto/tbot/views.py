from rest_framework import viewsets
import telegram


class BotViewSet(viewsets.GenericViewSet):
    """pass"""

    def send_message():
        bot = telegram.Bot(token='')

        # bot.send_message(
        #     text=f'''Новая ауди {data}
        #     ещё
        #     ''', 
        #     chat_id=
        #     )
        pass