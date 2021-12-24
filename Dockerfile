FROM python:3.8.10-slim-buster

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    g++ \
    libpq-dev \
    && apt-get clean \
    && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

CMD [ "gunicorn", "-b", "0.0.0.0:8001",  "-c", "python:gunicorn.config", "WebTemp.wsgi:application" ]
