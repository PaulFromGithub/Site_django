FROM python

WORKDIR /site_django_tb

COPY . /site_django_tb

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "site_tb/manage.py", "runserver"]