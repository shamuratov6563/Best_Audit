from django.contrib import admin
from .models import Rate, DescRate, Message
from modeltranslation.admin import TranslationAdmin


@admin.register(DescRate)
class DescRateAdmin(TranslationAdmin):
    list_display = ['tasks']


@admin.register(Rate)
class RateAdmin(TranslationAdmin):
    list_display = ['title', 'first', 'second', 'third']


@admin.register(Message)
class MessageAdmin(TranslationAdmin):
    list_display = ("name", "phone_number")
