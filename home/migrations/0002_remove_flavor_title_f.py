# Generated by Django 3.2 on 2022-07-25 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavor',
            name='title_f',
        ),
    ]
