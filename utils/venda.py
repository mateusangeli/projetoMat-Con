class Venda:
    def __init__(self, quantidade, produto):
        self.quantidade = quantidade
        self.produto = produto

    def getNomeProduto(self):
        return self.produto.nome

    def getValorUnitario(self):
        return self.produto.precovenda

    def getValor(self):
        return float(self.produto.precovenda) * float(self.quantidade)



