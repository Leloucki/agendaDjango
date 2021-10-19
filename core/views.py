from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

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

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    response = {'eventos':eventos}
    return render(request, 'agenda.html', response)

def index(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('user')
        password = request.POST.get('pass')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha invalido')
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        dataevento = request.POST.get('dataev')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo, data_evento=dataevento, descricao=descricao, usuario=usuario)
    return redirect('/')