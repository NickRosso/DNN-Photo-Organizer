# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
ADD /dependencies/pretrained_models.pytorch /code/dependencies/pretrained_models.pytorch
# Download http://data.lip6.fr/cadene/pretrainedmodels/nasnetalarge-a1897284.pth and store in classifier/.
ADD /classifier/nasnetalarge-a1897284.pth /root/.cache/torch/hub/checkpoints/nasnetalarge-a1897284.pth
RUN export TORCH_HOME="/code/classifier"
RUN pip install -r requirements.txt

WORKDIR /code/dependencies/pretrained_models.pytorch
# https://modelzoo.co/model/pretrained-modelspytorch
RUN python setup.py install

WORKDIR /code
COPY . /code/

