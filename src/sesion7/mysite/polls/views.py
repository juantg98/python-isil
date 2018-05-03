from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola DJANGO!")

def nombre(request):
   	return HttpResponse("Juan Tuya Garcia")