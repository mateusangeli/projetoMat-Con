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
        #self.setEventos()
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

    def setEventos(self):
        self.combo_clientes.currentIndexChanged.connect(self.index_changed_cliente)
        self.combo_produtos.currentIndexChanged.connect(self.index_changed_produto)
        self.btn_add_item.clicked.connect(self.addItem)

    def index_changed_cliente(self, i):
        print(self.lista_clientes[i].nome)
        self.clienteAtual = self.lista_clientes[i]
        self.id_lineEdit.setText(str(self.lista_clientes[i].id))

    def index_changed_produto(self, i):
        self.produtoAtual = self.lista_produtos[i]
        self.marca.setText(self.lista_produtos[i].marca)
        self.valor.setText(str(self.lista_produtos[i].precovenda))
        self.qtd_disp.setText(str(self.lista_produtos[i].quantidade))
        self.desc.setText(self.lista_produtos[i].descricao)

    def addItem(self):
        item = Venda(self.qtd.text(),self.produtoAtual)
        self.tabelaItens._addRow(item)

            