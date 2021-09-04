# ARQUIVO PRINCIPAL
import models.produtos_model as ProdModel
import models.clientes_model as CliModel
from utils.venda import Venda
import os


def printProdutos(lista):
    for l in lista:
        l.printInfo()

os.system('clear')
id_cliente = int(input("Digite o id do cliente: "))
cliente = CliModel.getCliente(id_cliente)
lista_produtos = ProdModel.getProdutos()
venda = Venda(-1, id_cliente)
while(True):
    os.system('clear')
    print("Cliente: ", cliente.nome)
    print("Quantidade de itens no carrinho: ", venda.qtdItens())

    #LISTA PRODUTOS
    print("\n\nLista de produtos: ")
    printProdutos(lista_produtos)

    # ESCOLHER O PRODUTO
    id_produto = int(input("Digite o id do produto: "))
    # ADICIONA ESSE PRODUTO NA LISTA DE VENDAS ( CARRINHO DE COMPRAS )
    produto = ProdModel.getProduto(id_produto)
    venda.addItem(produto)

    op = input("\n\nPara finalizar a compra digite [S]: ")
    if (op.upper() == 'S'):
        break

os.system('clear')
print("\n\nVenda finalizada")
print("Lista de itens: ")
prods = venda.getItens()
lista_produtos(prods)

print("\nValor Total: ", venda.valorTotal())