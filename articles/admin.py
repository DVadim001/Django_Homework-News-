from django.contrib import admin
from .models import News_article, News_comment

# Register your models here.
admin.site.register(News_article)
admin.site.register(News_comment)
