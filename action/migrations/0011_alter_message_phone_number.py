# Generated by Django 3.2.9 on 2021-12-12 14:23

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0010_auto_20211212_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
