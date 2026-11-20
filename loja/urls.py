from django.urls import path
from . import views

# Lista de rotas (URLs) específicas do aplicativo da loja
urlpatterns = [
    # Rota raiz do aplicativo ('') que aponta para a função lista_produtos criada nas views.
    # O parâmetro 'name='lista_produtos' serve para dar um apelido a essa rota e facilitar chamadas futuras.
    path('', views.lista_produtos, name='lista_produtos'),
]