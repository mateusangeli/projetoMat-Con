from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
import models.clientes_model as ClientesModel
import models.produtos_model as ProdModel
from ui.tabel_vendas import TebelaItens
from utils.item_venda import ItemVenda

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
        self.carregaDadosProdutos()
        self.tabelaItens = TebelaItens(self.tableWidget, self)

        qtd_validator = QRegExpValidator(QRegExp('^[1-9]{1}[0-9]{5}$'), self.qtd)
        self.qtd.setValidator(qtd_validator)


    def carregaDadosClientes(self):
        self.lista_clientes = ClientesModel.getClientes()
        lista_combo = []
        for c in self.lista_clientes:
            lista_combo.append(c.nome)
        self.combo_clientes.addItems(lista_combo)

    def carregaDadosProdutos(self):
        self.lista_produtos = ProdModel.getProdutos()
        lista_combo = []
        for c in self.lista_produtos:
            lista_combo.append(c.nomeP)
        self.combo_produtos.addItems(lista_combo)

    def setEventos(self):
        self.combo_clientes.currentIndexChanged.connect(
            self.index_changed_cliente)
        self.combo_produtos.currentIndexChanged.connect(
            self.index_changed_produto)
        self.btn_add_item.clicked.connect(self.addItem)
        self.btn_limpar_itens.clicked.connect(self.limparItens)
        self.btn_remover_item.clicked.connect(self.limparSelecionado)
        self.qtd.textEdited.connect(self.qtd_edited)

    def index_changed_cliente(self, i):
        self.clienteAtual = self.lista_clientes[i]
        self.id_lineEdit.setText(str(self.lista_clientes[i].id))

    def index_changed_produto(self, i):
        self.produtoAtual = self.lista_produtos[i]
        self.marca.setText(self.lista_produtos[i].marca)
        self.valor.setText(str(self.lista_produtos[i].precovenda))
        self.qtd_disp.setText(str(self.lista_produtos[i].quantidade))
        self.desc.setText(self.lista_produtos[i].descricao)

    def addItem(self):
        item = ItemVenda(self.qtd.text(),self.produtoAtual)
        self.tabelaItens._addRow(item)
        self.btn_limpar_itens.setEnabled(True)
        self.btn_add_item.setEnabled(False)
        self.qtd.setText("")

    def limparItens(self):
        self.tabelaItens.limparItens
    
    def limparSelecionado(self):
        self.tabelaItens.limparSelecionado()

    def qtd_edited(self, s):
        if s != "" and int(s) <= self.produtoAtual.quantidade:
            self.btn_add_item.setEnabled(True)
        else:
            self.btn_add_item.setEnabled(False)
    

            