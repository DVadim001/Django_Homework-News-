from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


app_name = 'articles'
urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about),
    path('contact-us', views.contacts),
    path('search', views.search_article),
    path('article/<int:pk>', views.article, name='article'),
    path('comment/<int:pk>', views.comment, name='comment'),
    path('not_found', views.article_not_found),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='articles/login.html'), name='login'),
    path('logout/', views.LogoutWithGetView.as_view(), name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]
