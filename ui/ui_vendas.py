from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
import models.clientes_model as ClientesModel
import models.produtos_model as ProdModel
from ui.tabel_vendas import TebelaItens
from utils.venda import Venda

class NovaVenda(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_vendas.ui", self)
        self.clienteAtual = None
        self.produtoAtual = None
        self.lista_clientes = []
        self.lista_produtos = []
        self.setEventos()
        self.carregaDadosClientes()
        self.carregaDadosProdutos
        self.tabelaItens = TebelaItens(self.tableWidget)

    def carregaDadosClientes(self):
        lista = ClientesModel.getClientes()
        lista_combo = []
        for c in lista:
            lista_combo.append(str(c.id)+ " - "+c.nome)
        self.combo_clientes.addItems(lista_combo)

    def carregaDadosProdutos(self):
        self.lista_produtos = ProdModel.getProdutos()
        lista_combo = []
        for p in self.lista_produtos:
            lista_combo.append(str(p.id) + " - "+p.nomeP)
        self.combo_produtos.addItems(lista_combo)
            