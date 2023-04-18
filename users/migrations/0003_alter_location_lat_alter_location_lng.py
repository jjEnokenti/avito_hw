# Generated by Django 4.1.7 on 2023-04-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=8, null=True),
        ),
    ]