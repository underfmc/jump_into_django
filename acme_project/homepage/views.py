# from django.shortcuts import render
from django.http import HttpResponse


# Главная страница.
def index(request):
    return HttpResponse('Главная страница')
