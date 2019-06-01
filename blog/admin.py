from django.contrib import admin
from  .models import Post, Category, Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'active', 'published')
    list_filter = ('active', 'updated')
    #search_fields = ('name', 'email', 'body')

class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published','status')
    list_filter = ('status', 'published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ['status', 'published']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, Postadmin)
admin.site.register(Category)