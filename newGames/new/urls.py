from django.urls import re_path
import new.views as news

app_name = 'new'

urlpatterns = [
    re_path('$', news.index, name='index'),
    re_path('hot_news/$', news.hot_news, name='hot_news'),
    re_path('categories/$', news.categories_news, name='categories_news'),
    re_path('cat/(?P<url_id>.*\s*)/$', news.category_news, name='category_news'),
    re_path('news/(?P<url_id>.*\s*)/$', news.news_page, name='page_news'),
]