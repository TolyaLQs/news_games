from django.contrib import admin

# Register your models here.

from user.models import User, SexUser, UserPhoto, FriendUser

admin.site.register(User)
admin.site.register(SexUser)
admin.site.register(UserPhoto)
admin.site.register(FriendUser)

