# from django.shortcuts import render
from django.http import HttpResponse


def product_list(request):
    return HttpResponse('Каталог товаров')


def product_detail(request, pk):
    return HttpResponse(f'Страница товара {pk}')
