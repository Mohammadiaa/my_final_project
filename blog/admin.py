from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_fields = ('name',) 

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'counted_view', 'published_date', 'created_date')
    list_filter = ('status', 'categories', 'tags', 'author')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published_date'
    filter_horizontal = ('categories', 'tags')
    ordering = ('-created_date',)
