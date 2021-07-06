from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from main.models import Galeria_agencia, Paquete_turistico_agencia,Servicios_agencia
from .forms import UserRegister
from django.contrib import messages
# Create your views here.
def index(request):
    paquetes=Paquete_turistico_agencia.objects.order_by('nombre')
    return render(request,"index.html",{'paquetes':paquetes})
def nosotros(request):
    return render(request,"acerca_nosotros.html")
def paquetes_turisticos(request):
    paquetes=Paquete_turistico_agencia.objects.order_by('nombre')
    return render(request,"paquetes_turisticos.html",{'paquetes':paquetes})
def paquete(request,slug):
    paquetes=Paquete_turistico_agencia.objects.filter(slug_paquete=slug)
    lista_paquetes=Paquete_turistico_agencia.objects.order_by('nombre')[:4]
    servicios=Servicios_agencia.objects.get_queryset().order_by('nombre')
    return render(request,"paquete.html",{'paquetes':paquetes,'lista_paquetes':lista_paquetes,'servicios':servicios})
def registro_user(request):
    if request.method == 'POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'Usuario {username} Registrado')
            return redirect('index')
    else:
        form=UserRegister()
    context={'form':form}


    return render(request,'registro.html',context)