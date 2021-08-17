import json

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import PeriodicTask, IntervalSchedule
# from setups.models import Order

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument('status', type=str)

	def handle(self, *args, **options):
		status = options['status']
		if status == 'run':
			PeriodicTask.objects.create(
					name= 'Repeat check',
					task='checking_auto',
					interval=IntervalSchedule.objects.get(every=10, period='seconds'),
                    args=json.dumps([options['status']]),
					start_time=timezone.now(),
					last_run_at = timezone.now(),
				)
		else:
			print('stop')
