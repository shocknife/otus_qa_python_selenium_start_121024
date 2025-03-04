FROM jenkins/jenkins

USER root

RUN apt update && apt install -y python3 python3-pip default-jre wget vim jq python3-venv

ARG ALLURE_VER=2.13.7

RUN wget https://github.com/allure-framework/allure2/releases/download/$ALLURE_VER/allure-$ALLURE_VER.tgz

RUN tar zxvf allure-$ALLURE_VER.tgz ; mv allure-$ALLURE_VER /usr/bin/allure-$ALLURE_VER

RUN ln -s /usr/bin/allure-$ALLURE_VER/bin/allure /usr/bin/allure

RUN rm -rf allure-$ALLURE_VER.tgz allure-$ALLURE_VER

USER jenkins