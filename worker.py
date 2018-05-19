from celery import Celery
from algorithm import approx

app = Celery(__name__, backend='rpc://', broker='redis://redis:6379/0')

@app.task
def integrate(*args, **kwargs):
    try:
        return approx(*args, **kwargs)
    except:
        return
