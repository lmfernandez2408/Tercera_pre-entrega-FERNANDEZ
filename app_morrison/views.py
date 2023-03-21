from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app_morrison/index.html")

def Inicio(request):
     return render(request, 'app_morrison/Inicio.html', {})

def Pedidos(request):
    return render(request, 'app_morrison/Pedidos.html', {})

def Clientes(request):
    return render(request, 'app_morrison/Clientes.html', {})

def Personal(request):
    return render(request, 'app_morrison/Personal.html', {})

def Formulario1(request):
    if request.method == 'POST':
        Clientes =  Clientes(request.post['Clientes'],(request.post['nombre','apellido']))
        Clientes.save()
        return render(request, "app_morrison/Clientes.html")

    return render(request, 'app_morrison/Formulario1.html')

def Formulario2(request):
    if request.method == 'POST':
        Personal =  Personal(request.post['Personal'],(request.post['nombre','apellido']))
        Personal.save()
        return render(request, "app_morrison/Personal.html")

    return render(request, 'app_morrison/Formulario2.html')

def Formulario3(request):
    if request.method == 'POST':
        Pedidos =  Mapa(request.post['Mapa'],(request.post['Tipo','Caracteristica']))
        Pedidos.save()
        return render(request, "app_morrison/Pedidos.html")

    return render(request, 'app_morrison/Formulario3.html')