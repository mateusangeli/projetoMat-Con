class ItemVenda:
    def __init__(self, quantidade, produto):
        self.quantidade = quantidade
        self.produto = produto

    def getNomeProduto(self):
        return self.produto.nomeP

    def getValorUnitario(self):
        return self.produto.precovenda

    def getValor(self):
        return "%.2f" % (float(self.produto.precovenda) * float(self.quantidade))