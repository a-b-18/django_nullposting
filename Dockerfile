# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install django-crispy-forms

COPY . .

EXPOSE 8000

CMD [ "python3", "-u", "manage.py", "runserver", "0.0.0.0:8000"]