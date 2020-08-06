FROM python:3.8

COPY Pipfile* /

RUN  pip3 install --no-cache-dir pipenv \
    && pipenv install --deploy --system --ignore-pipfile

WORKDIR /app
COPY . /app


CMD python main.py
