class Produto:
    def __init__(self, id, nome, marca, descricao, precocompra, precovenda, quantidade):
        self.id = id
        self.nome = nome
        self.marca = marca
        self.descricao = descricao
        self.precocompra = precocompra
        self.precovenda = precovenda
        self.quantidade = quantidade

    def print(self):
        info = [self.id, self.nome, self.marca, self.descricao, self.precocompra, self.precovenda, self.quantidade]
        print(info)
