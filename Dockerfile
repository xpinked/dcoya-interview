FROM python:3.10.10-buster

WORKDIR /usr/src/app

COPY ./backend/. .
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/usr/src/app

CMD [ "python", "main.py" ]