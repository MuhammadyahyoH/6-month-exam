# products/views.py
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from products.models import ProductModel, ProductCategory, ProductBrand


def list(request):
    products = ProductModel.objects.all()
    categories = ProductCategory.objects.all()
    brands = ProductBrand.objects.all()
    return render(request, 'products/shop.html', {
        'products': products,
        'categories': categories,
        'brands': brands,
    })


def detail(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    images = product.images.all()

    colors = product.products_quantity.select_related('colors').values_list(
        'colors__title', 'colors__code'
    ).distinct()

    sizes = product.products_quantity.select_related('sizes').values_list(
        'sizes__title', flat=True
    ).distinct()

    related_products = ProductModel.objects.filter(
        categories__in=product.categories.all()
    ).exclude(pk=pk).distinct()[:8]

    return render(request, 'products/detail.html', {
        'product': product,
        'images': images,
        'colors': colors,
        'sizes': sizes,
        'related_products': related_products,
    })








def wishlist(request):
    wishlist = request.session.get('wishlist', [])
    wishlist_items = ProductModel.objects.filter(pk__in=wishlist)
    return render(request, 'products/wishlist.html', {
        'wishlist_items': wishlist_items,
    })


def wishlist_add(request, product_id):
    product = get_object_or_404(ProductModel, pk=product_id)
    wishlist = request.session.get('wishlist', [])

    if product_id not in wishlist:
        wishlist.append(product_id)
        request.session['wishlist'] = wishlist

    return redirect(request.META.get('HTTP_REFERER', 'products:list'))


def wishlist_remove(request, product_id):
    wishlist = request.session.get('wishlist', [])

    if product_id in wishlist:
        wishlist.remove(product_id)
        request.session['wishlist'] = wishlist

    return redirect('products:wishlist')


