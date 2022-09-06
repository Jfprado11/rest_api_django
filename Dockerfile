FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python", "manage.py", "makemigrations"], ["python", "manage.py", "migrate"], ["python", "manage.py", "runserver"]
