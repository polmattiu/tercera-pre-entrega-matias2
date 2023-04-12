
from django.shortcuts import render, redirect
from inicio.forms import BuscarGastos, GastosFormulario
from inicio.models import Gasto

def mi_vista(request):
    return render(request, 'inicio/index.html')

def gastos_realizados(request):
    if request.method == "POST":
        formulario = GastosFormulario(request.POST)
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            gastos = Gasto(
                Tipo=datos_correctos['Tipo'],
                Articulo=datos_correctos['Articulo'],
                Cantidad=datos_correctos['Cantidad'],
                Precio=datos_correctos['Precio'],
            )
            gastos.save()
            return redirect('inicio:lista_de_gastos')
    formulario = GastosFormulario()
    return render(request, 'inicio/gastos_realizados.html', {'formulario': formulario})

def lista_de_gastos(request):
    tipo_a_buscar = request.GET.get('Tipo', None)
    articulo_a_buscar = request.GET.get('Articulo', None)
    cantidad_a_buscar = request.GET.get('Cantidad', None)
    precio_a_buscar = request.GET.get('Precio', None)
    if tipo_a_buscar:
        gastos = Gasto.objects.filter(Tipo__icontains=tipo_a_buscar)
    elif articulo_a_buscar:
        gastos = Gasto.objects.filter(Articulo__icontains=articulo_a_buscar)
    elif cantidad_a_buscar:
        gastos = Gasto.objects.filter(Cantidad=cantidad_a_buscar)
    elif precio_a_buscar:
        gastos = Gasto.objects.filter(Precio=precio_a_buscar)
    else:
        gastos = Gasto.objects.all()
    formulario_busqueda = BuscarGastos()
    return render(request, 'inicio/lista_de_gastos.html', {'gastos': gastos, 'formulario': formulario_busqueda})
