''''''
'''
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'blog/', include('blog.urls')) # 'blog/'- путь нашего приложения    hello - наша функция
]
Таким образом, любому URL-адресу, начинающемуся с admin/, Django будет находить соответствующее view (представление).


#from django.contrib import admin
from django.urls import path
from .views import index
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index) # 'blog/'- путь нашего приложения    hello - наша функция
]

from django.conf.urls import url, include
from . import views
# Указываем ссылку, по которой мы будем направлять пользователя на нужные нам приложения
urlpatterns = [
    url(r'^$', views.index, name='index'), # r'^$' - создааем основую страницу
    # url(r'^webexample/', include('webexample.urls')), # (То есть проверяет, есть ли такая ссылка)Увидит, что когда мы заходим на ссыдку webexample? подключает приложение и ищет файлик url
]z
'''
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',viewer,name='viewer_url')
]
