# specify the base image
FROM python:3-alpine3.15

# create a working directory
WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 3000

# CMD [ "python ./index.py" ]
CMD [ "python", "./index.py"]