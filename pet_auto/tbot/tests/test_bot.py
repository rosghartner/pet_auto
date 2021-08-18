from rest_framework import test, status

from pet_auto.tbot import views


class AutoAPITestCase(test.APITestCase):
    """Scheduler tests"""

    def setUp(self):
        pass

    def test_2(self):
        s = views.BotViewSet.send_message('hi')
        print('+')
