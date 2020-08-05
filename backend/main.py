import os

import uvicorn
from fastapi import FastAPI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

STATIC_DIR = os.path.join(PROJECT_DIR, 'static')


def get_application() -> FastAPI:
    application = FastAPI()
    return application


app = get_application()


@app.post('/hello/{name}')
def say_hello(name):
    return f"Hello {name}"


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', debug=True, reload=True)
