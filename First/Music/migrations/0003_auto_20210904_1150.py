# Generated by Django 3.1.7 on 2021-09-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipadress', models.GenericIPAddressField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='blog',
            name='ip_adress',
            field=models.ManyToManyField(to='Music.IpAdress'),
        ),
    ]