# Generated by Django 4.1.6 on 2023-02-09 14:58

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
