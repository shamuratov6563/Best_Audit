from modeltranslation.translator import register, TranslationOptions
from .models import Message, Rate, DescRate


@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = ('name', 'phone_number')


@register(Rate)
class RateTranslationOptions(TranslationOptions):
    fields = ('title', 'first', 'second', 'third')


@register(DescRate)
class DescRateTranslationOptions(TranslationOptions):
    fields = ('tasks',)

