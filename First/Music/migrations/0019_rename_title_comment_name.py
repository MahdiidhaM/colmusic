# Generated by Django 3.2.6 on 2021-09-06 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0018_auto_20210905_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='name',
        ),
    ]
