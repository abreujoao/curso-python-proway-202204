from django.shortcuts import render

def index(request):

    return render(request, 'users/index.html')

def detail(request, user_id):

    return render(render, 'users/detail.html')