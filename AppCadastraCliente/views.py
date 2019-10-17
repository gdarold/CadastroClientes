
from django.views.generic import TemplateView
from ProjetoCadastroCliente.models import Cliente
from django.views.generic import ListView

from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import UpdateView

# Create your views here.


class Index(TemplateView):
    template_name = "index.html"

class ListaClientes(ListView):
    template_name = "lista.html"
    model = Cliente
    context_object_name = 'cliente'
    

class CriaClientes(CreateView):
    template_name = "cria.html"
    model = Cliente()
    fields = '__all__'
    success_url = reverse_lazy("lista_clientes")
    
class ClientesDeleteView(DeleteView):
    template_name = "deleta.html"
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy("lista_clientes")
    
class AtualizaClientes(UpdateView):
    template_name = "atualiza.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("lista_clientes")


    