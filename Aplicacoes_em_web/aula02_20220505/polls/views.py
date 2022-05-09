from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question
from django.template import loader
*9
def index(request):
    #pegamos a lista das cinco perguntas mais recentes
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #tudo ate os primeiros 5
    #output = ', '.join([q.question_text for q in latest_question_list]) # List Comprehension

    #Criando o dicionario que será passado na rederização do template
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    question = Question.objets.get(pk= question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context=context)


def results(request, question_id):
    return HttpResponse(f"Você está olhando os resultados da pergunta {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na pergunta {question_id}.")
