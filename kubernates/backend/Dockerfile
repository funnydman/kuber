FROM funnydmantest/kube:backend.base

WORKDIR /kuber/backend
RUN git checkout master && git pull origin master

RUN pipenv install --deploy --system --ignore-pipfile

CMD python main.py


