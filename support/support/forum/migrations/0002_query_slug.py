# Generated by Django 3.0.8 on 2020-07-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
