from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
import uuid

# Create your models here.


class UnicodeEmailValidator(validators.RegexValidator):
    regex = r'^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$'
    message = 'Enter a valid email. This value may contain only letters,' \
              ' numbers, and @/./+/-/_ characters.'
    flags = 0


class SexUser(models.Model):
    sex = models.CharField(verbose_name='Пол', max_length=15, blank=True)

    def __str__(self):
        return f'{self.sex}'


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password is must !")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email_validator = UnicodeEmailValidator()
    username = None
    email = models.EmailField(verbose_name='Email',
                              max_length=150, unique=True,
                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                              validators=[email_validator],
                              error_messages={'unique': 'Пользователь с этой почтой зарегестрирован.'})
    last_name = None
    avatar = models.ImageField(verbose_name='Аватарка',
                               blank=True, null=True, default='users/ava.png', upload_to='users/ava_%Y%m')
    moderator = models.BooleanField(verbose_name='Модератор', default=False)
    first_name = None
    age = models.SmallIntegerField(verbose_name='Возраст', blank=True, null=True)
    date_add = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    url_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Имя', max_length=40,)
    sex = models.ForeignKey(SexUser, verbose_name='Пол', blank=True, null=True, on_delete=models.CASCADE)
    about_user = models.TextField(verbose_name='О себе', max_length=250, blank=True, null=True)
    objects = UserAccountManager()
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['date_add', 'name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserPhoto(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='user_photo', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фото пользователя', upload_to='user_photo')


class FriendUser(models.Model):
    user_friend = models.ForeignKey(User, verbose_name='Пользователь', related_name='user_friend', on_delete=models.CASCADE)
    friend_user = models.ForeignKey(User, verbose_name='Друг', related_name='friend', on_delete=models.CASCADE)

