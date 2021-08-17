from celery import shared_task
from django_celery_beat.models import PeriodicTask
from pet_auto.auto_api.views import AutoSearchViewSet



@shared_task(name="checking_auto")
def checking_auto():
	AutoSearchViewSet.search()
	print('1')