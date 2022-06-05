# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /usr/src/main

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./main/requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
# COPY ./main/entrypoint.sh .

# copy project
COPY ./main .

# run entrypoint.sh
# ENTRYPOINT ["./main/entrypoint.sh"]