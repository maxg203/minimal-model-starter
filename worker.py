from celery import Celery
from algorithm import approx

app = Celery(__name__, backend='rpc://', broker='redis://redis:6379/0')
integrate = app.task(approx)
