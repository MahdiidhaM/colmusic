# Generated by Django 3.1.7 on 2021-09-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0004_auto_20210904_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='ip_adress',
            field=models.ManyToManyField(blank=True, related_name='ip_adress', to='Music.IpAdress'),
        ),
    ]
