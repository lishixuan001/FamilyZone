# Generated by Django 2.0.7 on 2018-07-23 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0005_auto_20180723_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='life.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='life.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='job_title',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='workplace',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
