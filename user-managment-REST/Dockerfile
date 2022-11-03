FROM python:3-alpine
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


EXPOSE 8000
ENTRYPOINT python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
