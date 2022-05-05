from django.urls import path

# importamos o módulo views que está no mesmo diretorio de urls.py
from.import views

urlpatterns = [
    path('', views.index, name='index')
]
