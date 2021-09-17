# Generated by Django 3.2.6 on 2021-09-14 07:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0032_auto_20210914_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ManyToManyField(to='Music.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.blog')),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.ipadress')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='Music.Article', to='Music.IpAdress'),
        ),
    ]
