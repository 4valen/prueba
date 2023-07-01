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
    return render(request, 'inicio.html')
       

def contacto(request):
    return render(request, 'contacto.html')



def nosotros(request):
    return HttpResponse(layout+"""<h1> nosotros </h1>
     
</head>
<body>
  
    <main>
        <h2>Bienvenidos a nuestra página web</h2>
        <p>¡Hola! Esta es una página de ejemplo para mostrar información sobre nosotros y nuestros servicios.</p>
        <p>Si tienes alguna pregunta o deseas contactarnos, visita la página de <a href="#">Contacto</a>.</p>
        
    </main>
    """)

def donaciones(request):
    return HttpResponse(layout+"""<h1> donaciones </h1>
    <h1>DONACIONES</h1>
<h1>perros sin hogar</h1>
<a href="perrossh.html"><img src="perros sh.png" a/></a>
<h1>gatos sin hogar</h1>
<a href="gatossh.html"><img src="gatosSH.jpg" a/></a>
<!--Pie de página-->
<footer class="container">
    """)

def tienda(request):
    return HttpResponse(layout+"""<h1> tienda </h1>

<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="styleT.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous" type="module"></script>


        <style>
        .navbar-title {
            display: inline-block;
            margin-right: 10px;
        }
    </style>
    <script type="text/javascript">
    window.onload = function() {
            document.getElementById("boton").addEventListener("click", comprar);
        }

        function comprar() {
            var num1 = parseInt(document.getElementById("num1").value);
            var num2 = parseInt(document.getElementById("num2").value);
            var num3 = parseInt(document.getElementById("num3").value);
            var num4 = parseInt(document.getElementById("num4").value);
            var num5 = parseInt(document.getElementById("num5").value);
            var suma = num1+num2+num3+num4+num5;

            alert("Has añadido  nuevo articulo: " + suma);
        }
    </script>
    
</head>
<body>
    <header>
       
    </header>
    <body font-family="Helvetica Neue sans-serif">
        <script>
            function showAlert() {
                alert('¡has selecionado un articulo muy especial el cual tiene mucho detalle!');
            }
        </script>
        <script>
        function showAlert1() {
            alert('¡has selecioonado un articulo muy especial el cual tiene mucho detalle!');
        }
        </script>
        <section id="nosotros" class="pt-md-5">
            <h2 class="text-center my-5">Tienda</h2>
            <div class="container">
                <div class="row gy-3">
                    <div class="col-md-4">
                        <div class="card">
                            <img src="img1.png" class="card-img-top" alt="..." width="300px" height="300" id="im">
                            <div class="card-body">
                                <button class="boton" value="comprar" onclick="comprar()">Comprar</button>
                                <input type="text" id="num1"><br>
                                <button onclick="showAlert()">detalle</button>
                               
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                            <img src="img2.png" class="card-img-top" alt="..."  width="300px" height="300" id="im">
                            <div class="card-body">
                                <button onclick="showAlert()">detalle</button>
                                <button class="boton" value="comprar" onclick="comprar()"  id="boton">Comprar</button>
                                <input type="text" id="num2"><br>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                            <img src="img3.jpg" class="card-img-top" width="300px" height="300" id="im">
                            <div class="card-body">
                                <button onclick="showAlert()">detalle</button>
                                <input type="text" id="num3"><br>
                                <input type="button" value="Comprar" onclick="comprar();" id="boton">                    
                            </div>
                        </div> 
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                            <img src="imagen4.jpg" class="card-img-top" alt="..." width="300px" height="300" id="im">
                            <div class="card-body">
                                <button onclick="showAlert()">detalle</button>
                                <input type="text" id="num4"><br>
                                <button class="boton" value="comprar" onclick="comprar()">Comprar</button>                    
                            </div>
                        </div> 
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                            <img src="imagen5.jpg" class="card-img-top" alt="..." width="300px" height="300" id="im">
                            <div class="card-body">
                                <button onclick="showAlert()">detalle</button>
                                <input type="text" id="num5"><br>
                                <button class="boton" value="comprar" onclick="comprar()">Comprar</button>                   
                            </div>
                        </div> 
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                            <img src="imagen6.jpg" class="card-img-top" alt="..." width="300px" height="300" id="im">
                            <div class="card-body">
                                <button onclick="showAlert()">detalle</button>
                                <input type="text" id="num6"><br>
                                <button class="boton" value="comprar" onclick="comprar()">Comprar</button>                   
                            </div>
                        </div> 
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                            <img src="imagen7.jpg" class="card-img-top" alt="..." width="300px" height="300" id="im">
                            <div class="card-body">
                                <button onclick="showAlert()">detalle</button>
                                <input type="text" id="num7"><br>         
                                <button class="boton" value="comprar" onclick="comprar()">Comprar</button>                   
                            </div>
                        </div> 
                    </div>
                </div>
          
            </div>
    
        </section>
        <section id="faq" class="py-md-5">
    
        </section>
    """)

