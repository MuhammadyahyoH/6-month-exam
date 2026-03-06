from django.shortcuts import render

def home_page_view(request):
    return render(request,'home.html')

def category_page_view(request):
    return render(request,'category.html')