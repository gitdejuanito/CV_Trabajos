# Generated by Django 4.1.6 on 2023-02-03 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_alter_familia_equipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone', models.FloatField()),
            ],
        ),
    ]