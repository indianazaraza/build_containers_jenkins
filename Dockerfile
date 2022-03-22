FROM python:3.9-alpine3.14

COPY . .
RUN pip3 install pymongo
