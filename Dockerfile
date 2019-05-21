FROM python:3.6.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-docker
WORKDIR /django-docker
RUN apt-get update -y \
    && apt-get upgrade -y
ADD requirements.txt /django-docker/
RUN pip install -r requirements.txt
ADD . /django-docker/