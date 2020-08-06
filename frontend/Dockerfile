FROM funnydmantest/kube:frontend.base

RUN git clone https://github.com/funnydman/kuber.git /kuber/

WORKDIR /kuber/frontend
RUN yarn install

CMD yarn build


