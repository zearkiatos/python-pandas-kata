FROM python:alpine3.16

COPY . /app/

RUN apk add g++ jpeg-dev zlib-dev libjpeg make
RUN pip3 install pandas

WORKDIR /app