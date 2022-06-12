# Generated by Django 3.0.14 on 2022-06-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220610_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_created', models.DateField(auto_created=True)),
                ('fname', models.CharField(default=20, max_length=20)),
                ('lname', models.CharField(default=20, max_length=20)),
                ('username', models.CharField(default=20, max_length=20)),
                ('email', models.CharField(default=20, max_length=100)),
                ('password', models.CharField(default=20, max_length=50)),
            ],
        ),
    ]
