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

### 3. `django_celery/django_celery/__init__.py` 수정

추후 다른 앱에서 `@shared_task` 를 사용하기 위해 아래의 코드를 추가합니다.

```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

### 4. `broker_url` 설정

`app.config_from_object()` 설정에서 `namespace='CELERY'` 를 해주었기 때문에,  
장고 settings.py 에서 celery와 관련된 모든 설정은 CELERY로 시작해야 합니다.

따라서 settings.py에 다음과 같이 세팅해 줍니다. (rabbitmq container는 띄어져있다 가정합니다.)

```python
# settings.py
...
CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
```

### 5. celery worker 띄우기

```sh
celery -A django_celery worker --loglevel=INFO --concurrency=1
```

> --concurrency 설정을 안하면 머신의 core 수와 동일한 프로세스로 생성합니다.


### 6. django shell로 `debug_task` 실행

![image](https://user-images.githubusercontent.com/12469427/99144716-86eeeb80-26ab-11eb-91ac-ab52d5636098.png)

> 장고 쉘 화면


![image](https://user-images.githubusercontent.com/12469427/99144827-81de6c00-26ac-11eb-9c79-b1fe2c1c3b4d.png)

> worker 가 task 실행한 화면

### 7. shared_task 작업

먼저 test_app 을 만들어 여기에 shared_task 를 만들어 보겠습니다.

```sh
django-admin startapp test_app
```

```python
# django_celery/test_app/tasks.py
from celery import shared_task


@shared_task
def natural_sum(limit: int = 1000000):
    result: int = 0
    for i in range(1, limit + 1):
        result += i
    print(result)
    return result
```

그리고 장고에 test_app을 등록해 줍니다.

```python
# django_celery/django_celery/settings.py

INSTALLED_APPS = [
    ...,
    'test_app',
]
```

### 8. shared_task 확인

6번과 같이 확인하실 수 있습니다.

![image](https://user-images.githubusercontent.com/12469427/99145223-4f367280-26b0-11eb-9549-c7ea2e209509.png)

### +. celery multi로 데몬화 실행

```sh
celery -A django_celery multi start 1 --loglevel=INFO -c1 \
	--pidfile=/var/run/celery/%n.pid \
	--logfile=/var/log/celery/%n%I.log
```

## References

- [Celery Docs: First steps with Django](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)
