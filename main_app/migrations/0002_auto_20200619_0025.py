# Generated by Django 3.0.7 on 2020-06-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='pop',
            name='group',
        ),
        migrations.AddField(
            model_name='pop',
            name='groups',
            field=models.ManyToManyField(to='main_app.Group'),
        ),
    ]
