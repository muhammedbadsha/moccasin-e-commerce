FROM python:3.8-buster

ENV PYTHONUNBOFFERED 1

WORKDIR /moccasin

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
