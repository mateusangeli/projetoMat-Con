class Venda:
    def __init__(self, id, cliente, lista_de_itens, valortotal):
        self.id = id
        self.cliente = cliente
        self.lista_de_itens = lista_de_itens
        self.valortotal = valortotal


    def qtdItens(self):
        return len(self.lista_de_itens)

    def getItens(self):
        return self.lista_de_itens

    def valorTotal(self):
        return self.valortotal


