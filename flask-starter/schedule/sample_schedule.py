import  json

from app import app
from models import db, user

from . import scheduler

#interval examples
@scheduler.task("interval", id="do_job_1", seconds=30)
def job1():
    print("Job 2 executed")


#cron examples
@scheduler.task("cron", id="do_job_2", minute="3")
def job2():
    print("Job 2 executed")


