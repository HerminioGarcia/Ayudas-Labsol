# Generated by Django 4.0.2 on 2022-08-11 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_rename_user_datospersonales_userd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datospersonales',
            old_name='userD',
            new_name='user',
        ),
    ]