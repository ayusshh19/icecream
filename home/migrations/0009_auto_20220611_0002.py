# Generated by Django 3.0.14 on 2022-06-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]