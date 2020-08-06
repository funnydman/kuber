import os

import psycopg2
import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

STATIC_DIR = os.path.join(PROJECT_DIR, 'static')

main_router = APIRouter()

DATABASE = {
    'dbname': 'app',
    'user': 'postgres',
    'host': 'db',
    'password': 'postgres'

}

conn = psycopg2.connect(**DATABASE)


@main_router.get('/api/v1/get-data')
def root():
    with conn.cursor() as curr:
        curr.execute("select * from data_src;")
        return curr.fetchall()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost/api/"
]


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(main_router)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', debug=True, reload=True)
