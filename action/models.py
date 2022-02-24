from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from phone_field import PhoneField


class Message(models.Model):
    name = models.CharField(max_length=200)
    phone_number = PhoneField(blank=False)

    def __str__(self):
        return self.name


class Videos(models.Model):
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[FileExtensionValidator( allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title


class Rate(models.Model):
    title = models.CharField(max_length=100)
    first = models.CharField(max_length=100, null=True, blank=True)
    second = models.CharField(max_length=100, null=True, blank=True)
    third = models.CharField(max_length=100, null=True, blank=True)
    prize = models.CharField(max_length=20)

    class Meta:
        db_table = 'rate'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rate_detail', args=[str(self.pk)])

