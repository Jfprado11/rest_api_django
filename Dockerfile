
FROM python:3.8-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
RUN mkdir -p /app
COPY ./requirements.txt /requirements.txt
COPY . ./app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt

ENV PATH="/py/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8080

# Gunicorn as app server
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 api_workplace.wsgi:application
