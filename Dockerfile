FROM python:3.8.10-slim 

WORKDIR /app 

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:5000 app:app
