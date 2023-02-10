from django.urls import re_path
import new.views as new

app_name = 'user'

urlpatterns = [
    re_path('index/$', news.index, name='login'),
    re_path('hot_news/$', news.hot_news, name='register'),
    re_path('categories/$', news.categories, name='edit'),
    re_path('cat/(?P<url_id>.*\s*)/$', news.category, name='logout'),
    re_path('news/(?P<url_id>.*\s*)/$', news.news_page, name='profile'),
]