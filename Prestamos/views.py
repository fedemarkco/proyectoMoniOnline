from django.contrib.auth.decorators import login_required
from Prestamos.models import PedidoDePrestamos
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .checkPrestamo import checkStatus
from django.shortcuts import render, redirect
from .forms import Formulario


def formulario(request):
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()
            dni = form["dni"].value()
            response = checkStatus(dni)
            return render(request, "formResp.html", {"response": response})
        else:
            return render(request, "formPrestamo.html", {"form": form})
    else:
        form = Formulario()

    return render(request, "formPrestamo.html", {"form": form})


def loginView(request):
    if request.method == "POST":
        usuario = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect("listarPedidos")
        else:
            mensajeError = "Datos incorrectos."
            return render(request, "loginAdmin.html",
                          {"mensajeError": mensajeError})
    else:
        if request.user.is_authenticated:
            return redirect("listarPedidos")
        return render(request, "loginAdmin.html")


@login_required
def logoutView(request):
    logout(request)
    return redirect("loginView")


@login_required
def listarPedidos(request):
    pedidos = PedidoDePrestamos.objects.all()
    return render(request, "listaPedidosDePrestamo.html", {"pedidos": pedidos})


@login_required
def eliminarPedido(request, idPres):
    idP = PedidoDePrestamos.objects.get(id=idPres)
    if request.method == "POST":
        idP.delete()
        return redirect("listarPedidos")
    else:
        data = {"idP": idP.id, "nomApe": idP.__str__()}
        return render(request, "eliminarPedido.html", data)


@login_required
def editarPedido(request, idPres):
    idP = PedidoDePrestamos.objects.get(id=idPres)
    if request.method == "POST":
        form = Formulario(request.POST, instance=idP)
        if form.is_valid():
            form.save()
            return redirect("listarPedidos")
        else:
            return render(request,
                          "editarPrestamo.html",
                          {"form": form, "idP": idP.id})
    else:
        form = Formulario(instance=idP)
        return render(request,
                      "editarPrestamo.html",
                      {"form": form, "idP": idP.id})
