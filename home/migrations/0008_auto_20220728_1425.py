# Generated by Django 3.2 on 2022-07-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icon',
            old_name='icons_field',
            new_name='website',
        ),
        migrations.AddField(
            model_name='icon',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
