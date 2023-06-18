FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django
COPY . /django/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install django-currentuser
RUN pip install django-filter
RUN pip install openpyxl