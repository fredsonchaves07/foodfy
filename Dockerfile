FROM python:3

WORKDIR /usr/app

COPY . . 

RUN rm -f .secrets.toml

RUN rm -f .env

RUN pip install poetry

RUN poetry install

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]