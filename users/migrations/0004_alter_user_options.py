# Generated by Django 4.1.7 on 2023-04-07 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_location_lat_alter_location_lng'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-username'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
