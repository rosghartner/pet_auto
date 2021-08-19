from celery.schedules import crontab

from pet_auto.celery import app
from pet_auto.tbot import views

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
	# Calls test('hello') every 10 seconds.
	sender.add_periodic_task(crontab(minute=5, hour=10, day_of_week='monday'), hamster, name='hamster notice')
	sender.add_periodic_task(crontab(minute=0, hour='9, 16, 22'), cats_fish, name='cats, fish notice')
	sender.add_periodic_task(crontab(minute=5, hour=9), medicine_s, name='medicine_s notice')
	sender.add_periodic_task(crontab(minute=0, hour=13), medicine_p, name='medicine_p notice')#reworked later
	sender.add_periodic_task(crontab(minute=0, hour=22), medicine_p, name='medicine_p1 notice')


	#calls
	
	

@app.task()
def hamster():
    views.NoticeViewSet.hamster_notice()

@app.task()
def cats_fish():
    views.NoticeViewSet.cats_fish_notice()

@app.task()
def medicine_s():
	views.NoticeViewSet.medicine_notice_s()

@app.task()
def medicine_p():
	views.NoticeViewSet.medicine_notice_p()



