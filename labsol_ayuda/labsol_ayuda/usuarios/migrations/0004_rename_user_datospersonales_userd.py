# Generated by Django 4.0.2 on 2022-08-11 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_rename_userd_datospersonales_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datospersonales',
            old_name='user',
            new_name='userD',
        ),
    ]
