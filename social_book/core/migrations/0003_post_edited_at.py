# Generated by Django 4.2 on 2023-04-20 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_at',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
