from django.urls import path

from . import views, nombre, lista 

urlpatterns = [
    path('', views.index, name='index'),
]
#from . import nombre
urlpatterns = [
    path('', nombre.nom, name='nombre'),
]
#from . import lista
urlpatterns = [
    path('', lista.lis, name='lista'),
]	