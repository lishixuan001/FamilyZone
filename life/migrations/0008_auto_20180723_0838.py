# Generated by Django 2.0.7 on 2018-07-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0007_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.CharField(default='Anonymous', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='workplace',
            field=models.CharField(default='Anonymous', max_length=40),
        ),
    ]
