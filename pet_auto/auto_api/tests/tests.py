from django.test import TestCase
from rest_framework import test, status

from pet_auto.auto_api import views


class AutoAPITestCase(test.APITestCase):
    """Scheduler tests"""

    def setUp(self):
        pass

    def test_1(self):
        s = views.AutoSearchViewSet.search()
        print('+')
