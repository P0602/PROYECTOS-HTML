from django.shortcuts import render
from appgestion.models import Despacho
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,"index.html")


def listar(request):
    return render(request,"listar.html")

def ingresar(request):
    return render(request,"ingresar.html")


def eliminar(request):
    return render(request,"eliminar.html")


def modificar(request):
    return render(request,"modificar.html")

def filtro(request):
    return render(request, "filtro.html")

def indicador(request):
    return render(request, "indicador.html")

def registrar(request):
    numero_recibido=request.GET["txt_numero"]
    nombre=request.GET["txt_nombre"]
    direccion=request.GET["txt_direccion"]
    telefono=request.GET["txt_telefono"]
    productos=request.GET["txt_productos"]
    peso=request.GET["txt_peso"]
    medidas=request.GET["txt_medidas"]
    fecha_ingreso=request.GET["txt_fecha_ingreso"]
    fecha_envio=request.GET["txt_fecha_envio"]
    estado=request.GET["txt_estado"]
    if len(numero_recibido)>0 and len(nombre)>0 and len(direccion)>0 and len(telefono)>0 and len(productos)>0 and len(peso)>0 and len(medidas)>0 and len(fecha_ingreso)>0 and len(fecha_envio)>0 and len(estado)>0:
        desp=Despacho(numero_despacho=numero_recibido,nombre_cliente=nombre,direccion=direccion,celular=telefono,productos=productos,peso=peso,medidas=medidas,fecha_ingreso=fecha_ingreso,fecha_envio=fecha_envio,estado=estado)
        desp.save()
        alerta="Despacho ingresado..."
    else:
        alerta="Despacho no ingresado..."
    return HttpResponse(alerta)

def listar_despacho(request):
    datos = Despacho.objects.all()
    return render(request,"listar.html",{'Despacho':datos})

def eliminar_despacho(request):
    if request.GET["txt_numero"]:
        numero_recibido = request.GET["txt_numero"]
        despacho = Despacho.objects.filter(numero_despacho=numero_recibido)
        if despacho:
            des=Despacho.objects.get(numero_despacho=numero_recibido)
            des.delete()
            mensaje = "Despacho eliminado correctamente..."
        else:
            mensaje = "No existe despacho con ese numero"
    else:
        mensaje = "debe ingresar el numero de despacho a eliminar"
    return HttpResponse(mensaje)


def modificar_despacho(request):
    if request.GET["txt_numero"]:
        numero_recibido = request.GET["txt_numero"]
        estado_recibido = request.GET["txt_estado"]
        despacho = Despacho.objects.filter(numero_despacho=numero_recibido)
        if despacho:
            des=Despacho.objects.get(numero_despacho=numero_recibido)
            des.estado = estado_recibido
            des.save()
            mensaje = "Estado de despacho modificado correctamente"           
        else:
            mensaje = "No existe despacho con ese numero"           
    else:
        mensaje = "Debe ingresar el numero de despacho a modificar"
    return HttpResponse(mensaje)