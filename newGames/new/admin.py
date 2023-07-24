from django.contrib import admin
from .models import News, NewsLike, NewsPhotosController
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'pub_date', 'pub_updated')
    list_display_links = ('title',)
    list_filter = ('published', 'pub_date')

