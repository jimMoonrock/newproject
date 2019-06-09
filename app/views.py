''''''
'''
{% extends "mainApp/wrapper.html"%} <!--Теперь мы унаследовали код -->

{% block content %}
<p>Проверрка работоспособности</p>

{% include "mainApp/includes/some_html.html "%} <!-- include - можем вставлять куда вставлять -->
{% include "mainApp/includes/some_html.html "%} <!-- include - можем вставлять куда вставлять -->
{% include "mainApp/includes/some_html.html "%} <!-- include - можем вставлять куда вставлять -->
{% endblock %}

from django.http import HttpResponse

def index(request):
    return HttpResponse()

которая принимает request в качестве аргумента и возвращает (return) результат работы функции render, 
которая уже соберёт наш шаблон страницы 

  {% block content %}

    {% endblock %}
    
    
 from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

def posts_list(request):
    return HttpResponse('<h1>hello world!</h1>')
    
    <!-- --> - комментарий в html
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Index page</title>
</head>
<body>
    <h1>Hello world</h1>
    <h2>Wassup</h2>
    <!-- {{ names }} - вывели список имен-->
    {% for name in names %} <!-- Начала цикла начинается -->
        <P>
            {{ name }}
        </P>
    {% endfor %} <!-- Заканчивается цикл for -->
</body>
</html>


Как создавать посты новые  в python manage.py shell


Cначала импортируем
from blog.models import Post


p = Post(title='New post', slug='new-slug', body='new post body')
p.save
p.id

Лучшая алитернативна созданию поста
p1 = Post.objects.create(title='new post2', slug='new-post2', body='body')


Таким образом вызвать все созданные модели
Post.objects.all()



как осуществить поиск объектов с помощью метода get (look up)
post = Post.objects.get(slug__iexact='New slug')

pos1 = Post.objects.filter(slug__contains='new')   
'''
'''
def posts_list(request):
    # names = ['Oleg', 'Masha','Olja','Ksu']
    posts = Post.objects.all()
    # return render(request, 'blog/index.html', context={'names':names})
    return render(request, 'blog/index.html',context={'posts':posts})

def post_detail(request, slug): # Создаем функцию для detail
    post = Post.objects.get(sluf__iexact=slug) # получаем объект с slug
    return render(request, 'blog/post_detail.html', context={'post'})

# Хотим показать пользователю че здесь происходит, 
  # context = {'name':n} n - тут Пользователь олег, то что мы вставили в шаблон в index.html c помощию context={'name':n}
  # и получили значение ключа 'name' В файле index.html
  
Процесс выполнения шаблона данных называется Рендеринг(render)  или проще когда у меня в html подставляются мои значения
'''


from django.urls import path
from django.shortcuts import render
def viewer(request):
    #  return render(request, 'app/index.html',context={'names':names})
    names = ['Valera','Max','John','Ron']
    return render(request, 'app/basic.html')