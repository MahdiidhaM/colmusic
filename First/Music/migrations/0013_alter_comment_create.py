# Generated by Django 3.2.6 on 2021-09-05 06:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0012_auto_20210905_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
