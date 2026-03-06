from django.urls import path
from shared.views import home_page_view, category_page_view, product_page_view, blog_page_view, elements_page_view, \
    about_us

app_name = 'shared'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('category/', category_page_view, name='category'),
    path('product/', product_page_view, name='product'),
    path('blog/', blog_page_view, name='blog'),
    path('elements/', elements_page_view, name='elements'),
    path('about/', about_us, name='about_us'),
]