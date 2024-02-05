from django.db import models

# Create your models here.


# Таблица Новостей.
class News_article(models.Model):
    news_title = models.CharField('заголовое новости', max_length=256)
    news_text = models.TextField('текст новости')
    news_date = models.DateTimeField('дата добавления', auto_now_add=True)
# news_photo = models.ImageField(upload_to='news_photo')

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# Таблица комментариев
class News_comment(models.Model):
    comment = models.ForeignKey(News_article, on_delete=models.CASCADE)
    comment_author = models.CharField('имя автора', max_length=256)
    comment_text = models.TextField('текст комментария')
    comment_date = models.DateTimeField('дата комментария', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comment_author
