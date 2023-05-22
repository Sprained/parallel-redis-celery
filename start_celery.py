import subprocess

from app import celery

queues = celery.control.inspect().active_queues()


if queues:
    for queue_name, _ in queues.items():
        subprocess.Popen(
            [
                "celery",
                "-A",
                "app.celery",
                "worker",
                "--queues={}".format(queue_name),
            ]
        )
