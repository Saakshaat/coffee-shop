FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install --no-cache-dir fastapi

COPY ./app /rest-service
WORKDIR /rest-service
CMD ["uvicorn", "entry:app", "--host", "0.0.0.0", "--port", "80"]