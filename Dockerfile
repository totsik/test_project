FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install unixodbc unixodbc-dev -y
RUN apt-get update

RUN mkdir project

COPY ./requirements.txt /project/requirements.txt

WORKDIR /project

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /project

EXPOSE 8000