# Generated by Django 3.2.7 on 2021-09-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official_use', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='official_use.Category'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='end_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
