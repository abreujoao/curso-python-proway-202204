from django.views import generic
from ..models import Tag

class IndexView(generic.ListView):

    model=Tag

    #essa parte faz que nao precisamos fazer tudo a mao, o django faz sozinho.