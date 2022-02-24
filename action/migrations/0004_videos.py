# Generated by Django 3.2.9 on 2021-11-09 19:39

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0003_alter_message_phone_number'),
    ]

    operations = [
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
    ]