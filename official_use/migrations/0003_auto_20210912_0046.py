# Generated by Django 3.2.7 on 2021-09-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official_use', '0002_auto_20210912_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
