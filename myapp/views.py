from django.shortcuts import render, redirect, get_object_or_404
from .models import Mueble, Cliente, Venta
from .forms import MuebleForm, ClienteForm, VentaForm, MuebleFilterForm
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio.html')

def registrar_mueble(request):
    if request.method == 'POST':
        form = MuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = MuebleForm()
    
    return render(request, 'registrar_mueble.html', {'form': form})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado exitosamente.')
            return redirect('inicio')
    else:
        form = ClienteForm()

    return render(request, 'registrar_cliente.html', {'form': form})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            try:
                venta = form.save()
                messages.success(request, f'Venta registrada exitosamente. Total: ${venta.total:.2f}')
                return redirect('inicio')
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = VentaForm()

    return render(request, 'registrar_venta.html', {'form': form})

def resumen_inventario(request):
    form = MuebleFilterForm(request.GET or None)
    muebles = Mueble.objects.all()

    if form.is_valid():
        categoria = form.cleaned_data.get('categoria')
        min_stock = form.cleaned_data.get('min_stock')

        if categoria:
            muebles = muebles.filter(categoria=categoria)
        if min_stock is not None:
            muebles = muebles.filter(stock__gte=min_stock)

    context = {
        'form': form,
        'muebles': muebles,
    }
    return render(request, 'resumen_inventario.html', context)

def historial_ventas_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    ventas = Venta.objects.filter(cliente=cliente).order_by('-fecha_venta')

    context = {
        'cliente': cliente,
        'ventas': ventas,
    }
    return render(request, 'historial_ventas_cliente.html', context)

def perfil_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    context = {
        'cliente': cliente,
    }
    return render(request, 'perfil_cliente.html', context)

def lista_clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
    }
    return render(request, 'lista_clientes.html', context)