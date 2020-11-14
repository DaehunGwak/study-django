# 2. Django 와 Celery 조합 첫 걸음 

Django 와 Celery를 어떻게 조합해서 쓰는지 정리

## django + celery (@shared_task)

### 1. Django 초기화

```sh
django-admin startproject django_celery
```

### 2. `django_celery/django_celery/celery.sh` 추가

Django settings.py 파일을 사용하여 Celery 앱을 초기화하는 부분

```python
import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

### 3. `worker `


## References

- [Celery Docs: First steps with Django](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)
