from django.urls import path
from . import views

app_name= 'blogs'

urlpatterns = [
    path('<int:blogs_id>/', views.detail, name='detail'),
    path('posts/', views.index, name='index')
]