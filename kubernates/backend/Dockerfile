FROM funnydmantest/kube:backend.base

RUN git clone https://github.com/funnydman/kuber.git /kuber/

WORKDIR /kuber/backend
RUN ls
RUN pipenv install --deploy --system --ignore-pipfile

CMD python main.py


