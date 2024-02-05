from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.home),
    path('about-us', views.about),
    path('contact-us', views.contacts),
    path('search', views.search_article),
    path('article/<int:pk>', views.article, name='article'),
    path('comment/<int:pk>', views.comment, name='comment'),
    path('not_found', views.article_not_found),


]
