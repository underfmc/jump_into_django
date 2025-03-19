from django.shortcuts import render


# Главная страница.
def index(request):
    template_name = 'homepage/index.html'
    return render(request, template_name)
