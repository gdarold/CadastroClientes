from django.urls import path
from AppCadastraCliente.views import Index, ListaClientes, AtualizaClientes, \
    CriaClientes, ClientesDeleteView
from ProjetoCadastroCliente.models import Cliente

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('clientes/', ListaClientes.as_view(), name="lista_clientes"),
    path('clientes/cadastrar/', CriaClientes.as_view(model=Cliente), name="cadastra_clientes"),
    path('clientes/<pk>', AtualizaClientes.as_view(model=Cliente), name="atualiza_clientes"),
    path('clientes/excluir/<pk>', ClientesDeleteView.as_view(), name="deleta_clientes"),
    
]
