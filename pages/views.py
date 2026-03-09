from django.shortcuts import render
from .models import BannerType

from django.shortcuts import render
from .models import SliderModel, BannerModel
from products.models import ProductModel
from blogs.models import BlogAuthorModel


def home(request):
    sliders = SliderModel.objects.filter(is_active=True)
    banners = BannerModel.objects.filter(is_active=True, banner_type=BannerType.CATEGORY)
    intro_banners = BannerModel.objects.filter(is_active=True, banner_type=BannerType.INTRO)[:2]


    all_products = ProductModel.objects.all()[:8]

    furniture_products = ProductModel.objects.filter(
        categories__title__icontains='furniture'
    )[:8]
    decor_products = ProductModel.objects.filter(
        categories__title__icontains='decor'
    )[:8]
    lighting_products = ProductModel.objects.filter(
        categories__title__icontains='lighting'
    )[:8]

    return render(request, 'pages/home.html', {
        'sliders': sliders,
        'banners': banners,
        'intro_banners': intro_banners,
        'all_products': all_products,
        'furniture_products': furniture_products,
        'decor_products': decor_products,
        'lighting_products': lighting_products,
    })

def about(request):
    authors = BlogAuthorModel.objects.filter(is_active=True)
    return render(request, 'pages/about.html', {'authors': authors})

from .models import ContactModel

def contact(request):
    error = None
    success = False

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not full_name or not email or not message:
            error = 'Name, email and message are required.'
        else:
            ContactModel.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                subject=subject,
                message=message,
            )
            success = True

    return render(request, 'pages/contact.html', {
        'error': error,
        'success': success,
    })

def faq(request):
    return render(request, 'pages/faq.html')

def coming_soon(request):
    return render(request, 'pages/coming-soon.html')