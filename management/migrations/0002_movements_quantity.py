# Generated by Django 3.2.4 on 2021-06-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movements',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]