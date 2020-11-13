from celery import Celery


app = Celery('tasks', broker="pyamqp://guest@localhost//")


@app.task
def natural_sum(limit: int = 1000000):
    result: int = 0
    for i in range(1, limit + 1):
        result += i
    print(result)
    return result
