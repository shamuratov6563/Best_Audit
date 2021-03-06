# Generated by Django 4.0.3 on 2022-03-18 05:30

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DescRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(max_length=200)),
                ('tasks_ru', models.CharField(max_length=200, null=True)),
                ('tasks_uz', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('name_uz', models.CharField(max_length=200, null=True)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('phone_number_ru', phone_field.models.PhoneField(max_length=31, null=True)),
                ('phone_number_uz', phone_field.models.PhoneField(max_length=31, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_ru', models.CharField(max_length=100, null=True)),
                ('title_uz', models.CharField(max_length=100, null=True)),
                ('first', models.CharField(blank=True, max_length=100, null=True)),
                ('first_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('first_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('second', models.CharField(blank=True, max_length=100, null=True)),
                ('second_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('second_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('third', models.CharField(blank=True, max_length=100, null=True)),
                ('third_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('third_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('prize', models.CharField(max_length=20)),
                ('descs', models.ManyToManyField(to='action.descrate')),
            ],
            options={
                'db_table': 'rate',
            },
        ),
    ]
