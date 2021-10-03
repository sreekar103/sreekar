FROM python:3.9.1-buster
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt --upgrade pip
CMD ["uwsgi", "app.ini"]
