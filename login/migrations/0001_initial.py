# Generated by Django 4.0 on 2021-12-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
