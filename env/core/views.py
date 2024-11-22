from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }
    return render(request, 'teste.html', context) #index.html

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    produto = Produto.objects.filter(pk=pk)
    context = {'produto': produto}

    return render(request, 'produto.html', context)