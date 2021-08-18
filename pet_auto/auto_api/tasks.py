from celery.schedules import crontab

from pet_auto.auto_api.views import AutoSearchViewSet
from pet_auto.celery import app

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
	# Calls test('hello') every 10 seconds.
	sender.add_periodic_task(crontab(minute='*/2'), checking_auto, name='checking auto')
	# sender.add_periodic_task(10.0, checking_auto2, name='add every 10')
	#calls
	
	

@app.task()
def checking_auto():
	AutoSearchViewSet.search()
	print('1')

@app.task()
def checking_auto2():
	# AutoSearchViewSet.search()
	print('2')






