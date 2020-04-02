FROM python:3.6.10-alpine3.11

COPY ./requirements.txt /var/www/app/

WORKDIR /var/www/app

RUN pip install -r /var/www/app/requirements.txt

ENTRYPOINT ["python"]

CMD ["run.py"]

EXPOSE 5000
