from django.urls import re_path
import user.views as user

app_name = 'user'

urlpatterns = [
    re_path('login/$', user.user_login, name='login'),
    re_path('register/$', user.user_register, name='register'),
    re_path('edit/$', user.user_edit, name='edit'),
    re_path('logout/$', user.user_logout, name='logout'),
    re_path('profile/(?P<url_id>.*\s*)/$', user.user_profile, name='profile'),
]