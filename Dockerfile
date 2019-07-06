FROM python:3.7-alpine3.10

WORKDIR /app
EXPOSE 8181

RUN pip install pipenv==2018.11.26
COPY Pipfile Pipfile.lock ./
RUN pipenv install  --deploy --system --ignore-pipfile

COPY hello_world/ ./hello_world

CMD ["python", "./hello_world/main.py"]