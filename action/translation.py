from modeltranslation.translator import register, TranslationOptions
from .models import Message, Rate


@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = ('name', 'phone_number')


@register(Rate)
class RateTranslationOptions(TranslationOptions):
    fields = ('title', 'first', 'second', 'third')


