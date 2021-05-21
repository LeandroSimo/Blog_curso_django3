from django.http.response import HttpResponse
from django.shortcuts import render



def hello_blog(request): 
    lista = ["Curso","teste","teste","teste","teste","teste","teste",]
    data = {"name": "Curso de Django 3", "lista_tecnologias": lista}
    return render(request, "index.html", data)
