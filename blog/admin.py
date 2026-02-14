from django.contrib import admin
from .models import Post, Category, Tag, Comment
from django_summernote.admin import SummernoteModelAdmin
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
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'counted_view', 'published_date', 'created_date')
    list_filter = ('status', 'categories', 'tags', 'author')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published_date'
    filter_horizontal = ('categories', 'tags')
    ordering = ('-created_date',)
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_date', 'approved') 
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Mark selected comments as approved"

