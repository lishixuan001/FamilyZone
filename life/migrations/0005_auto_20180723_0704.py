# Generated by Django 2.0.7 on 2018-07-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0004_auto_20180723_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=50),
        ),
    ]
