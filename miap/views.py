from django.shortcuts import render , HttpResponse

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


def holaMundo(request):
    return HttpResponse(layout+"""<h1>hola mundo con django</h1>
    <p> aqui presentamos l</p>""")


def inicio(request):
    return HttpResponse(layout+"""<h1> inicio </h1>
     <p> aqui presentamos 2</p>""")

def contacto(request):
    return HttpResponse(layout+"""<h1> contacto </h1>
    <p> aqui presentamos 3""")

def nosotros(request):
    return HttpResponse(layout+"""<h1> nosotros </h1>""")

def donaciones(request):
    return HttpResponse(layout+"""<h1> donaciones </h1>""")

def tienda(request):
    return HttpResponse(layout+"""<h1> tienda </h1>""")

