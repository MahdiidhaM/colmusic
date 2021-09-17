# Generated by Django 3.2.6 on 2021-09-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0017_rename_ipaddress_ipadress_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='hits',
        ),
        migrations.AddField(
            model_name='blog',
            name='hit',
            field=models.ManyToManyField(blank=True, related_name='hit', through='Music.Article', to='Music.IpAdress'),
        ),
    ]
