# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
#VOLUME /crawler
#WORKDIR /ch
COPY . .

RUN apt-get -y update
RUN apt-get -y upgrade


RUN pip install scrapy && \
    pip install selenium && \    
    apt install ./google-chrome-stable_current_amd64.deb -y