# Generated by Django 3.2.4 on 2021-06-15 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20210616_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movements',
            name='location_from',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_from', to='management.locations'),
        ),
        migrations.AlterField(
            model_name='movements',
            name='location_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_to', to='management.locations'),
        ),
        migrations.AlterField(
            model_name='movements',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.products'),
        ),
    ]
