from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout

# Create your views here.
layout="""
<h1>sitio web con django</h1>

<ul>
    <li><a href="/inicio">Inicio</a>
    <li>
    <li> <a href="/contacto"> contacto</a>
    <li>
    <li> <a href="/nosotros"> nosotros</a>
    <li>
    <li> <a href="/donaciones"> donaciones</a>
    <li>
     <li> <a href="/tienda"> tienda</a>
    <li>

    <li> <a href="/hola-mundo">hola mUndo</a>
    <li>
</ul>
<hr>
"""
      
        
            

def index(request):
    return HttpResponse(layout+"""<h1> inicio S </h1>
    """)


def clientesadd(request):
    return render(request, 'alumnos/clientesadd.html')


def inicio(request):
    return render(request, 'inicio.html')
       

def contacto(request):
    return render(request, 'contacto.html')


def nosotros(request):
    return render(request, 'nosotros.html')

def donaciones(request):
    return render(request,'donaciones.html')

def tienda(request):
    return render(request,'tienda.html')
def login(request):
    if request.metod =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username,password=password)
    if user is not None:
            login(request,user)
            return redirect('inicio')                 
 

def register_page(request):

    register_form =UserCreationForm()
    if request.method=='POST':
        register_form =UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()

            return redirect('login')



       
def region(request):
    return render(request,'region.html')



    return render(request, 'user/register.html',{
        'title':'Registro',
        'register_form':register_form
        })
    

