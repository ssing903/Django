from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post)

# Customing the way models are being displayed on the server
@admin.register(Post)
class YesAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status','created','updated')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')

