# Generated by Django 3.2.6 on 2021-09-13 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0021_blog_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='hit',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='IpAdress',
        ),
    ]