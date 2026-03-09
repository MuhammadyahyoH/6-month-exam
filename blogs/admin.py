from django.contrib import admin
from .models import BlogModel, BlogCategoryModel, BlogTagModel, BlogAuthorModel, BlogViewModel


@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)


@admin.register(BlogTagModel)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(BlogAuthorModel)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'bio')


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title',)
    filter_horizontal = ('category', 'tag')


@admin.register(BlogViewModel)
class BlogViewAdmin(admin.ModelAdmin):
    list_display = ('user_ip', 'blog', 'created_at')