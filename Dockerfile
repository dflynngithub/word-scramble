# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "src/scrmabled_strings.py", "--dictionary", "input/dictionary.inp", "--input", "input/input.inp"]