# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
ADD /dependencies/pretrained-models.pytorch /code/dependencies/pretrained-models.pytorch
RUN export TORCH_HOME="/code/classifier"
RUN pip install -r requirements.txt

WORKDIR /code/dependencies/pretrained-models.pytorch
# https://modelzoo.co/model/pretrained-modelspytorch
RUN python setup.py install

WORKDIR /code
COPY . /code/

