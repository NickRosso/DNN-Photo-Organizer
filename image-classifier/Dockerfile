# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

ADD pretrained-models.pytorch /code/pretrained-models.pytorch
RUN pip install -r requirements.txt
# https://modelzoo.co/model/pretrained-modelspytorch
WORKDIR /code/pretrained-models.pytorch
RUN python setup.py install

COPY . /code/


CMD ["python", "pretrained-models.pytorch/examples/imagenet_logits.py", "-a" "nasnetalarge", "--path_img", "data/cat.jpg"]