from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class PostsList(ListView):

    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, по которому будем сортировать (указываем, что сортировка будет по убыванию создания)
    ordering = "-date_of_post"
    # Указываем имя шаблона, в котором будут содержаться все инструкции
    template_name = "news.html"
    # Имя списка, в котором лежат все наши новости, нужно для обращения в html-шаблоне
    context_object_name = "posts"
    
    Post.objects.all()


class PostDetail(DetailView):

    # Модель используем ту же
    model = Post
    # Шаблон будет другим
    template_name = "new.html"
    # Название объекта, в котором будет выбранная новость
    context_object_name = "post"

    # Этот метод позволяет изменять набор данных, передающихся в шаблон
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context["time_now"] = datetime.utcnow()

        return context
