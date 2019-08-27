from django.shortcuts import render

# Create your views here.

def retornar_index(request):
    return render(request,'index.html')

def retornar_prox(request):
    return render(request,'prox.html')   