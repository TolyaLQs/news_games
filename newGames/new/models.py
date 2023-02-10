from django.db import models
from user.model import User
# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    content = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    published = models.BooleanField(verbose_name='Статус', default=False)
    pub_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    image = models.ImageField(verbose_name='Фото', upload_to='news/')

    def __str__(self):
        return self.title

    def save_news(self):
        self.save()


class NewsLike(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
