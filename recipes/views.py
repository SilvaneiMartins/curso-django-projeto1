from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')
