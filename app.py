from celery import Celery

celery = Celery(
    __name__, broker="redis://redis:6379", backend="redis://redis:6379"
)


@celery.task
def devine(x, y):
    import time

    time.sleep(5)
    return x / y
