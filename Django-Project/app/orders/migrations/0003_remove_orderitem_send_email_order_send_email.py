# Generated by Django 4.2.11 on 2024-05-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_send_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='send_email',
        ),
        migrations.AddField(
            model_name='order',
            name='send_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email отправки'),
        ),
    ]
