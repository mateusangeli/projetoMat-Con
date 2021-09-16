class Produto:
    def __init__(self, id, nomeP, marca, descricao, precocompra, precovenda, quantidade):
        self.id = id
        self.nomeP = nomeP
        self.marca = marca
        self.descricao = descricao
        self.precocompra = precocompra
        self.precovenda = precovenda
        self.quantidade = quantidade

    def print(self):
        info = [self.id, self.nomeP, self.marca, self.descricao, self.precocompra, self.precovenda, self.quantidade]
        print(info)

    def printInfo(self):
        info = [self.id, self.nomeP, self.precovenda]
        print(info)