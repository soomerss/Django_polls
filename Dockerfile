FROM python:3.9.6

RUN pip3 install django

WORKDIR /User/giho.han/app

COPY . .

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]

EXPOSE 8000