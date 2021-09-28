class ItemVenda:
    def __init__(self, quantidade, produto, valor_unitario=None):
        self.quantidade = quantidade
        self.produto = produto
        self.valor_unitario = valor_unitario

    def getNomeProduto(self):
        return self.produto.nomeP

    def getValorUnitario(self):
        return self.produto.precovenda

    def getValor(self):
        return "%.2f" % (float(self.produto.precovenda) * float(self.quantidade))

    def novaQtd(self):
        return int("%.0f" % (int(self.produto.quantidade) - int(self.quantidade)))