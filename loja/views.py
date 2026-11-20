from django.shortcuts import render, redirect
from django.contrib import messages  
from .models import Produto
from .forms import PedidoForm

def lista_produtos(request):
    # Consulta todos os produtos cadastrados no catálogo
    produtos = Produto.objects.all()

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()  # Persiste a encomenda na tabela Pedido (SQLite)
            messages.success(
                request,
                'Encomenda registrada no CAFÉ TIA ROSA! Seu pedido já entrou na fila de preparo.'
            )
            # Redireciona após POST para evitar duplicidade ao atualizar a página
            return redirect('lista_produtos')
    else:
        form = PedidoForm()

    return render(request, 'loja/index.html', {
        'produtos': produtos,
        'form': form
    })