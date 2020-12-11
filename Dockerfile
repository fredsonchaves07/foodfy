FROM python:latest

WORKDIR /app
COPY app /app
COPY cmd.sh /
COPY requirements.txt /

EXPOSE 5000 3200

CMD ["/cmd.sh"]