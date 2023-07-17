FROM python:3.9

WORKDIR /app

COPY requirements.txt .
#RUN pip install -r requirements.txt
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
    libwebkit2gtk-4.0-dev


RUN pip install django
RUN pip install djangorestframework
RUN pip install drf-yasg
RUN pip install openbb-nightly
#RUN pip install pwry

COPY . .
EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000