from modeltranslation.translator import register, TranslationOptions
from .models import SliderModel, BannerModel


@register(SliderModel)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


@register(BannerModel)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'text')