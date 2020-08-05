import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return


@app.post('/hello/{name}')
def say_hello(name):
    return f"Hello {name}"


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
