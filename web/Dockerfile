FROM --platform=linux/amd64 python:3.11-slim AS build

WORKDIR /usr/app/src

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
