from django.db import models

# Modelo que representa os produtos da padaria (pães, bolos, salgados, etc.)
class Produto(models.Model):
    # Nome do produto (ex: Pão Francês) com limite de 100 caracteres
    nome = models.CharField(max_length=100)
    
    # Descrição detalhada dos ingredientes ou características do produto
    descricao = models.TextField()
    
    # Preço do produto com até 6 dígitos no total e 2 casas decimais (ex: 9999.99)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Campo booleano (True/False) para indicar se o produto está disponível para venda
    disponivel = models.BooleanField(default=True)

    # Função que retorna o nome do produto quando ele for listado no painel admin
    def __str__(self):
        return self.nome

# Modelo que registra os pedidos realizados pelos clientes
class Pedido(models.Model):
    # Nome do cliente que fez o pedido
    cliente_nome = models.CharField(max_length=100)
    
    # Telefone de contato do cliente
    telefone = models.CharField(max_length=20)
    
    # Chave estrangeira ligando o pedido a um produto específico do catálogo
    # Se o produto for excluído, o pedido associado é apagado (on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    # Quantidade de itens solicitados no pedido (valor inteiro positivo)
    quantidade = models.PositiveIntegerField(default=1)
    
    # Data e hora exata em que o pedido foi gerado (preenchido automaticamente)
    data_pedido = models.DateTimeField(auto_now_add=True)
    
    # Status para controlar se o pedido já foi separado/entregue (True) ou pendente (False)
    concluido = models.BooleanField(default=False)

    # Função para exibir uma identificação clara do pedido no sistema
    def __str__(self):
        return f"Pedido de {self.cliente_nome} - {self.produto.nome}"