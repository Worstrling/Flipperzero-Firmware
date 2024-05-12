FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

CMD sleep 10 \
    && python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root','root@test.ru','root')" \
    && python manage.py loaddata fixtures/goods/categories.json \
    && python manage.py loaddata fixtures/goods/products.json \
    && python manage.py collectstatic --no-input \
    && gunicorn app.wsgi:application --bind 0.0.0.0:8000