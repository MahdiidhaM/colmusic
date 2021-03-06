# Generated by Django 3.2.6 on 2021-09-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0014_remove_blog_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='Music.Article', to='Music.IpAdress'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
