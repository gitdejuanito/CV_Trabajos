# Generated by Django 4.1.6 on 2023-02-06 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
