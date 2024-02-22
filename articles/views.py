from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import News_article
from . import forms
from django.contrib.auth import logout
from django.views import View


# Отображение главной страницы (все новости)
def home(request):
    # Выполнение поиска
    search = forms.SearchForm()
    articles_news = News_article.objects.order_by('-news_date')[:5]
    # Передаём на фронт
    context = {'search': search, 'articles_news': articles_news}
    return render(request, 'articles/home.html', context)


# Страница О нас
def about(request):
    return render(request, 'articles/about.html')


# Страница контактов
def contacts(request):
    return render(request, 'articles/contacts.html')


# Страница одной новости
def article(request, pk):
    try:
        a = News_article.objects.get(id=pk)
    except:
        raise Http404('Новость не найдена.')
    comments = a.news_comment_set.order_by('-id')[:10]
    return render(request, 'articles/article.html', {'news': a, 'comments': comments})


# Поиск новостей по фильтру
def search_article(request):
    if request.method == 'POST':
        get_article = request.POST.get('search_article')
        articles = News_article.objects.filter(news_title__icontains=get_article)
        if articles:  # Это проверит, содержит ли QuerySet объекты
            # Если статей найдено, рендерим страницу с результатами поиска
            return render(request, 'articles/search_result.html', {'articles': articles})
        else:
            # Если статьи не найдены, перенаправляем на страницу 'not found'
            return redirect('/not_found')


# Новость не найдена
def article_not_found(request):
    return render(request, 'articles/not_found.html')


# Оставление комментария
def comment(request, pk):
    try:
        a = News_article.objects.get(id=pk)
    except:
        raise Http404('Новость не найдена.')
    a.news_comment_set.create(comment_author=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:article', args=(a.id,)))


# Регистрация
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:home')
    else:
        form = forms.SignUpForm()
    context = {'form': form}
    return render(request, 'articles/signup.html', context)


# Функция выхода
class LogoutWithGetView(View):
    def get(self, request):
        logout(request)
        return redirect('articles:home')

