from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    template_name="about/about.html"
    lista=[1,2,3,4,5]

    return render(request, template_name, {'miLista':lista})



        

