# Generated by Django 3.1.7 on 2021-09-04 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0007_auto_20210904_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='hits',
        ),
    ]