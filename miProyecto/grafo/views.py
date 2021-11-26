from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def grafos(request):
    tejidos=[1,2,3,4,5]
    resultado=extraeGrafo(tejidos)
    template_name="home/index.html"    

    diccionario={"resultado:":resultado}
    return render(request, template_name, diccionario)

def extraeGrafo(t):
    return