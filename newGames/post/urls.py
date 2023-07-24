from django.urls import re_path
import post.views as post

app_name = 'user'

urlpatterns = [
    re_path('$', post.all_post, name='all_post'),
]

