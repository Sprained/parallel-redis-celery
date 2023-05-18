from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/devine")
# async def add_devine():
#     devine.delay(1, 2)

# TODO: Dockenizar celery e flower
# celery -A celery.celery flower --port=5555
