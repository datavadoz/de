from celery import Celery

app = Celery('tasks', broker='')

@app.task
def add(x, y):
    return x + y
