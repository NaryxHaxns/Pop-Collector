# Generated by Django 3.0.7 on 2020-06-19 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200619_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='image',
        ),
    ]
