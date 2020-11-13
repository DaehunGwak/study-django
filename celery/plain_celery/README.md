# 1. 순수 Celery 예제

비동기 배치 잡을 장고로 구성해야되는 상황이 발생되어 실습하며 정리입니다.  
그 첫 번째로 Celery 만 사용하는 튜토리얼 따하며 정리합니다.

- [1. 순수 Celery 예제](#1-순수-celery-예제)
  - [Environments](#environments)
  - [Steps](#steps)
    - [0. 들어가기 전에](#0-들어가기-전에)
    - [1. broker (rabbitmq)](#1-broker-rabbitmq)
    - [2. celery 코드 작성](#2-celery-코드-작성)
    - [3. Celery Worker (consumer) 서버 실행](#3-celery-worker-consumer-서버-실행)
    - [4. python shell 로 실행해보기](#4-python-shell-로-실행해보기)
  - [References](#references)

## Environments

- celery 5.0.2
- rabbitmq (docker)
- python 3.6.12
- [more detail](./requirements.txt)

## Steps

### 0. 들어가기 전에

Celery를 쓰는 이유는, 시간이 오래걸리는 스크립트를 돌려야하는데 http에서 동기적으로 작업하면, 킵커넥션을 오래두고 있어야하고, 클라이언트에 피드백을 너무 느리게 줄 수 밖에 없습니다.

따라서 Celery로 비동기 작업(Job) 을 빼서 작업하기 위함이고, 이 작업을 처리해주는 Worker들은 Celery에서 멀티 스케일(오토 스케일도 가능)로 병렬적 실행이 가능하기 때문에 사용합니다.

그리고 broker를 사용하여 적절한 Worker들에게 job을 나누어 줄 수도 있습니다.

![image](https://user-images.githubusercontent.com/12469427/99068191-5a759980-25ef-11eb-8ec3-b596f6819893.png)
> Sender (장고, celery beat 와 같은) => Broker => Workers (Consumer)  
> 출처: [medium: [part3] push server (feat.Celery) by taek hwan Kwon](https://medium.com/@taekani/part-3-push-server-feat-celery-17b2c7f211cf)

### 1. broker (rabbitmq)

빠른 진행을 위해 docker 로 실행

```sh
docker run -it --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

도커로 실행 후 `ctrl` + `p` `q` 로 빠져나오고,  
브라우저에 `localhost:15672`로 접속하면 rabbitmq 확인 가능

![image](https://user-images.githubusercontent.com/12469427/99064442-5181c980-25e9-11eb-902b-76e142d3be8d.png)
> guest/guest(id/pw) 로 로그인 가능, 단 로컬에서만 동작하니 실제 production 구성 시 계정 설정 필요

### 2. celery 코드 작성

```python
# tasks.py
from celery import Celery

app = Celery('tasks', broker="pyamqp://guest@localhost//")

@app.task
def natural_sum(limit: int = 1000000):
    result: int = 0
    for i in range(1, limit + 1):
        result += i
    print(result)
    return result
```

### 3. Celery Worker (consumer) 서버 실행

> 저는 screen 으로 띄어 작업하였습니다.

```sh
celery -A tasks worker --loglevel=INFO
```

![image](https://user-images.githubusercontent.com/12469427/99066150-d5d54c00-25eb-11eb-8a88-7ee717247f44.png)

> 이런식으로 워커를 띄우게 되면 작성한 tasks 가 감지되어야 합니다.

### 4. python shell 로 실행해보기

아래와 같이 파이썬 쉘을 실행하여 task를 import 하여 실행하면 worker로 job을 보내게 됩니다. (저는 pycharm으로 콘솔 바로 띄었는데 `python` 커맨드만 입력하셔도 가능합니다.)

```python
>>> from tasks import natural_sum

>>> natural_sum.delay()
<AsyncResult: 645f92e1-9705-4410-b89a-c8b010c6f6c7>

>>> natural_sum.delay(333333333)
<AsyncResult: f96dfbe1-c4b2-4f5e-a023-9b6b1ac53534>
```

![image](https://user-images.githubusercontent.com/12469427/99066742-c7d3fb00-25ec-11eb-9f91-f3c49ec6a28f.png)
> Worker Server 결과화면

## References

- [Celery Docs: First Steps with Celery](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps)
- 구조도 출처: [medium: [part3] push server (feat.Celery) by taek hwan Kwon](https://medium.com/@taekani/part-3-push-server-feat-celery-17b2c7f211cf)
