# Generated by Django 4.1.6 on 2023-02-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
    ]
