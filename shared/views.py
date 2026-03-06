from django.shortcuts import render

def home_page_view(request):
    return render(request, 'shared/home.html')

def category_page_view(request):
    return render(request, 'layout/category.html')

def product_page_view(request):
    return render(request, 'products/product-lists.html')

def blog_page_view(request):
    return render(request, 'blogs/blog.html')

def elements_page_view(request):
    return render(request, 'layout/elements.html')

def about_us(request):
    return render(request, 'shared/about.html')