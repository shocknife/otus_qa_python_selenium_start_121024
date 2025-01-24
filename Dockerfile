FROM python:3.12-slim

WORKDIR /app

VOLUME /allure-results

RUN apt update && apt upgrade -y && apt install -y bash

RUN apt update && apt install -y netcat-traditional

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh

LABEL author=shocknife

#CMD ["./wait-for-it.sh", "172.19.0.4", "8080", "pytest", "-v", "tests/*", "--headless", "--base_url", "http://172.19.0.4:8080", "--browser", "chrome", "--executor", "172.19.0.2"]