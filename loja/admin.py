from django.contrib import admin
from .models import Produto, Pedido

# Registra o modelo Produto no painel de controle do Django
admin.site.register(Produto)

# Registra o modelo Pedido no painel de controle do Django
admin.site.register(Pedido)