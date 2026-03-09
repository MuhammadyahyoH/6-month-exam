from django.contrib import admin
from products.models import (ProductModel, ProductCategory, ProductBrand,
                             ProductSize, ProductColor, ProductQuantity, ProductImageModel)


class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 3


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 1


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount', 'is_new', 'is_discount')
    list_filter = ('categories', 'brand')
    search_fields = ('title',)
    filter_horizontal = ('categories',)
    inlines = [ProductImageInline, ProductQuantityInline]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')