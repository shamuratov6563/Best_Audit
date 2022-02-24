from django.contrib import admin
from .models import Rate, Videos, Message
from modeltranslation.admin import TranslationAdmin

admin.site.register(Videos)


@admin.register(Rate)
class RateAdmin(TranslationAdmin):
    list_display = ['title', 'first', 'second', 'third']


@admin.register(Message)
class MessageAdmin(TranslationAdmin):
    list_display = ("name", "phone_number")
