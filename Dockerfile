FROM python:3.10

WORKDIR /fastapi-app

COPY ./main/requirements.txt .

RUN pip install -r requirements.txt

COPY ./main ./main

CMD uvicorn main.app:app --host 0.0.0.0 --port 8000