# ARQUIVO PRINCIPAL
from models.clientes_model import *
lista_clientes = getClientes()

for clientes in lista_clientes:
    clientes.print()
