from fastapi import FastAPI

from app import celery, create_worker

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create")
async def create_queue():
    celery.send_task(
        "app.create_worker", kwargs={"name": "teste"}, queue="configs"
    )


# devine.delay(1, 2)
