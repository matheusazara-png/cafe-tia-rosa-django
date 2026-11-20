from django import forms
from .models import Pedido

# Formulário baseado no modelo Pedido para capturar os dados enviados pelo cliente
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        # Campos que o cliente irá preencher na tela de encomenda
        fields = ['cliente_nome', 'telefone', 'produto', 'quantidade']
        
        # Dicionário para personalizar os rótulos (labels) exibidos no HTML
        labels = {
            'cliente_nome': 'Seu Nome Completo',
            'telefone': 'Telefone/WhatsApp',
            'produto': 'Escolha o Produto',
            'quantidade': 'Quantidade',
        }
        
        # Adicionando classes CSS do Bootstrap para estilizar os campos do formulário automaticamente
        widgets = {
            'cliente_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Maria Silva'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (61) 99999-9999'}),
            'produto': forms.Select(attrs={'class': 'form-select'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'value': '1'}),
        }