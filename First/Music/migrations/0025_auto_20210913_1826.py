# Generated by Django 3.2.6 on 2021-09-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0024_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='hit',
        ),
        migrations.AddField(
            model_name='blog',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='Music.Article', to='Music.IpAdress'),
        ),
    ]
