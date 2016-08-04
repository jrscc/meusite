from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    saudacao = "BEM VINDO AS ENQUETES!!!! "
    return HttpResponse(saudacao)

