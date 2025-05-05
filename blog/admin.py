from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'content')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)