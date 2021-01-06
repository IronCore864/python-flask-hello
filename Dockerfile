FROM python:3.9-slim
MAINTAINER Tiexin Guo "guotiexin@gmail.com"
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
USER 1000
CMD gunicorn hello:app -w 2 -b 0.0.0.0:5000
