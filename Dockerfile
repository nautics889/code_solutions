FROM python:3.6.6-jessie
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-docker
WORKDIR /django-docker
RUN apt-get update -y \
    && apt-get upgrade -y\
    && apt-get install postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5 -y
ADD requirements.txt /django-docker/
RUN pip install -r requirements.txt
ADD . /django-docker/