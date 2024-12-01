from importlib.resources import contents
from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def teste(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }
    return render(request, 'teste.html', context) #index.html

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #Esse comando é melhor, pq já retorna o objeto ao invés de uma lista de objetos com o objeto dentro
    #Além de que quando não encontra o objeto, mostra erro 404
    produto = get_object_or_404(Produto, id = pk) 
    context = {'produto': produto}

    return render(request, 'produto.html', context)

def error404(request):
    template = loader.get_template('special/error404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('special/error500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)