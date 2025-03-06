FROM python:3.7.9-slim-stretch

COPY mysite/requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY mysite /app/