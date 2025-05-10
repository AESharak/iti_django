from django.contrib import admin
from .models import Post, Author, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'created_at')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at')
    search_fields = ('author_name', 'content')
    list_filter = ('created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)