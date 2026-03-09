from django.shortcuts import render, get_object_or_404
from .models import BlogModel


def list(request):
    blogs = BlogModel.objects.filter(status='PUBLISHED')
    return render(request, 'blogs/blog-list.html', {'blogs': blogs})


def detail(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)
    # Track view
    user_ip = request.META.get('REMOTE_ADDR')
    from .models import BlogViewModel
    BlogViewModel.objects.get_or_create(user_ip=user_ip, blog=blog)
    return render(request, 'blogs/blog-detail.html', {'blog': blog})