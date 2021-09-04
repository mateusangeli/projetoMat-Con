class Venda:
    def __init__(self, id, cliente):
        self.id = -1
        self.cliente = cliente
        self.produtos = [] #LISTA DE PRODUTOS

    def addItem(self, item):
        self.produtos.append(item)

    def qtdItens(self):
        return len(self.produtos)

    def getItens(self):
        return self.produtos

    def valorTotal(self):
        soma = 0
        for i in self.produtos:
            soma += i.precovenda
        return soma



