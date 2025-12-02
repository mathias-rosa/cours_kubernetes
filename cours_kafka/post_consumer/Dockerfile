FROM python:3.9.20-slim-bookworm

RUN pip install kafka

COPY ./post_consumer/ ./
CMD [ "python", "main.py"]