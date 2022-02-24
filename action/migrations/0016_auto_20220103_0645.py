# Generated by Django 3.2.9 on 2022-01-03 06:45

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0015_auto_20211212_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='name_tu',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='phone_number_en',
            field=phone_field.models.PhoneField(max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='phone_number_tu',
            field=phone_field.models.PhoneField(max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='first_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='first_tu',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='second_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='second_tu',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='third_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='third_tu',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='title_tu',
            field=models.CharField(max_length=100, null=True),
        ),
    ]