FROM python:3.9

ARG DIR=/coffee-shop/rest-service/

WORKDIR ${DIR}

# this is copied before the entire directory to cache installations irrespective of code changes
COPY app/Pipfile ${DIR}

RUN pip install pipenv
RUN pipenv install

COPY app/ ${DIR}
EXPOSE 80

CMD ["pipenv", "run", "uvicorn", "entry:app", "--host", "0.0.0.0", "--port", "80"]
