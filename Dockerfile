FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -Ur requirements.txt

COPY . /app

CMD python3 -m eduu
