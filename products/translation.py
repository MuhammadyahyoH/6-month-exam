from modeltranslation.translator import register, TranslationOptions
from products.models import ProductModel, ProductCategory


@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)