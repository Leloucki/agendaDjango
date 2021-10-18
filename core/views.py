from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.models import Evento


# def getLocalByTitle(titulo_evento):
#     return HttpResponse(f'<h1>{Evento.local.get(titulo=titulo_evento)}</h1>')

# def lista_eventos(request):
#     evento = Evento.objects.get(id=1)
#     response = {'evento':evento}
#     return render(request, 'agenda.html', response)

# def lista_eventos(request):
#     eventos = Evento.objects.all()
#     response = {'eventos':eventos}
#     return render(request, 'agenda.html', response)

def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    response = {'eventos':eventos}
    return render(request, 'agenda.html', response)

def index(request):
    return redirect('/agenda/')