# Generated by Django 4.1.6 on 2023-02-07 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_remove_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
