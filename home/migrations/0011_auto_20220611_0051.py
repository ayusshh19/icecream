# Generated by Django 3.0.14 on 2022-06-10 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220611_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='last_login',
            new_name='lastlogin',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='no_login',
            new_name='nologin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='account_created',
            new_name='accountcreated',
        ),
    ]
