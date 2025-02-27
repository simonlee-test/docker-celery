import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docker_celery.settings")
app = Celery("docker_celery")
                        # in settings.py, look for any attributes start with the word CELERY
app.config_from_object("django.conf:settings", namespace="CELERY")

#expose this task to celery
@app.task
def add_numbers(): 
    return 

#it will look for tasks.py of each django app
app.autodiscover_tasks()
