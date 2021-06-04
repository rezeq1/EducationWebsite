FROM python:3.8

ENV PYTHONDONTWRITEBYCOME 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN pip install channels
RUN pip install channels-redis
RUN pip install coverage

RUN pip freeze
COPY . /code

EXPOSE 8000 
CMD ["python","manage.py","runserver","127.0.0.1:8000"]
