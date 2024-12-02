from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.
def inicio_vistaProductos(request):
    losProductos=Productos.objects.all()
    return render(request,"gestionarProductos.html", {"misProductos":losProductos})

def registrarProductos(request):
    id_producto=request.POST["numid_producto"]
    nombre=request.POST["txtnombre"]
    marca=request.POST["txtmarca"]
    tela=request.POST["txttela"]
    talla=request.POST["numtalla"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    
    guardarProductos=Productos.objects.create(
        id_producto=id_producto,nombre=nombre,marca=marca,tela=tela,talla=talla,
        precio=precio,stock=stock
    ) #GUARDA EL REGISTRO
    
    return redirect("productos")

def seleccionarProductos(request,id_producto):
    productos=Productos.objects.get(id_producto=id_producto)
    return render(request, "editarProductos.html",{"misProductos":productos, "misProductos":productos})

def editarProductos(request):
    id_producto=request.POST["numid_producto"]
    nombre=request.POST["txtnombre"]
    marca=request.POST["txtmarca"]
    tela=request.POST["txttela"]
    talla=request.POST["numtalla"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    
    productos=Productos.objects.get(id_producto=id_producto)
    productos.nombre=nombre
    productos.marca=marca
    productos.tela=tela
    productos.talla=talla
    productos.precio=precio
    productos.stock=stock
    productos.save() #guarda registro actualizado
    return redirect("productos")

def borrarProductos(request,id_producto):
    productos=Productos.objects.get(id_producto=id_producto)
    productos.delete() # borra el registro
    return redirect("productos")