from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.safestring import mark_safe
from user.models import User
import datetime
# Create your models here.


def path_image():
    return f'news/{str(datetime.datetime.now()).split()[0]}'


class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Текст', blank=True, null=True)
    pub_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    pub_add = models.DateTimeField(verbose_name='Дата публикации', default=datetime.datetime.now(),
                                   blank=True, null=True)
    published = models.BooleanField(verbose_name='Статус', default=False)
    pub_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    image = models.ImageField(verbose_name='Фото', blank=True, upload_to=path_image())

    def __str__(self):
        return self.title

    def len_content(self):
        return True if len(self.content) >= 150 else False

    def save_news(self):
        self.save()

    def check_date(self):
        now = datetime.datetime.now()
        if self.pub_add > now:
            self.published = True

    def get_image(self):
        if not self.image:
            return '/static/images/owl-gray.svg'
        return self.image.url
        # method to create a fake table field in read only mode

    def check_like_user(self, user):
        try:
            self.check = NewsLike.objects.filter(user__id=user, news__id=self.id).count()
            if self.check > 0:
                self.check = True
                return self.check
            else:
                self.check = False
                return self.check
        except:
            self.check = False
            return self.check

    def check_likes(self):
        try:
            return NewsLike.objects.filter(id=self.id).count()
        except:
            return 0

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_image())

    class Meta:
        ordering = ['published', '-pub_add']
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class NewsPhotosController(models.Model):
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото', upload_to='news')

    class Meta:
        ordering = ['news']
        verbose_name = 'Доп. фото'
        verbose_name_plural = 'Доп. фотографии'


class NewsLike(models.Model):
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        ordering = ['news', 'user']
        verbose_name = 'Лайки'
        verbose_name_plural = 'Лайки'


class CommentNews(models.Model):
    text = models.TextField(verbose_name='Текст', blank=True, null=True)

