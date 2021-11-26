from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Tessiu

# Create your views here.
def home(request):
    tejidos=Tessiu.objects.get_queryset()
    resultado=mifuncion(tejidos)
    template_name="home/index.html"    

    diccionario={'lista':tejidos, "resultado:":resultado}
    return render(request, template_name, diccionario)

def mifuncion(L):
    
    #df=np.array([[j,2:5]])
    #lista2=[{'r1':j,'r2':i,'conectado':'si'
    #        if abs(df.iloc[j,2:5]-df.iloc[i,2:5]).sum()<5
    #        else 'no'}
    #       for j in range(0,4)
    #       for i in range(j+1,5)]


    return "Hola"

def nohome(request):
    print("Saludos a la banda")
    template_name="home/index.html"
    return render(request, template_name, {})
    

def procesaLista(lista):
    #Hacer algo con la lista
    lista1=[]
    for elemento in lista:
        valor=elemento.temperatura**2 + elemento.inflammation**2 + elemento.color**2
        if valor > 50:
            lista1.append(valor**0.5)
    return lista1
