# Generated by Django 4.1.7 on 2023-05-05 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_initial'),
        ('selection', '0002_alter_selection_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ads.ad'),
        ),
    ]
