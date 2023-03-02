# base image
FROM python:3.10.6-slim-buster

WORKDIR /app

# env variables:
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile.* /app/

# copy project
COPY . /app/

EXPOSE 8000

# install pipenv and all the packages in Pipfile
RUN pip install -r requirements.txt
