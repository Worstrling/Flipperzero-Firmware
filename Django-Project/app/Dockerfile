FROM python:3.12

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root','root@test.ru','root')" \
    && python manage.py loaddata fixtures/goods/categories.json \
    && python manage.py loaddata fixtures/goods/products.json \
    && python manage.py runserver 0.0.0.0:8000