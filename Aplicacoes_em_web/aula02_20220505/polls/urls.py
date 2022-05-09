from django.urls import path

# importamos o módulo views que está no mesmo diretorio de urls.py
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote',views.vote, name='vote')
]
