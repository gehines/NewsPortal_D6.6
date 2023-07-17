from django.urls import path
# Импортируем наши представления
from .views import PostsList, PostDetail


urlpatterns = [
    path('', PostsList.as_view()),  # при помощи метода as_view представляем наш класс в виде функции
    path('<int:pk>', PostDetail.as_view()),  # pk - первичный ключ, выводящийся в шаблоне
                                             # (pk можем переназначить в нашем представлении,
                                             # наследуемом от класса DetailView: pk_url_kwargs = '***',
                                             # в этой переменной по умолчанию стоит 'pk';
                                             # int - указывает на целочисленные значения
]
