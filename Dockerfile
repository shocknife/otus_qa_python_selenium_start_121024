FROM python:3.12-alpine

WORKDIR /app

VOLUME /allure-results

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh

LABEL author=shocknife

CMD ["./wait-for-it.sh", "opencart", "8080", "pytest", "-v", "tests/*", "--no-sandbox", "--headless", "--base_url", "http://localhost:8080", "--browser", "chrome", "--browser_version", "128.0", "--executor", "selenoid"]