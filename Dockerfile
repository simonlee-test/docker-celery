FROM python:3.12.8-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1 \ 
    PYTHONUNBUFFERED 1

RUN pip install -U pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]