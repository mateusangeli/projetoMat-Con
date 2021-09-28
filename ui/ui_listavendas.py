from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon
from ui.ui_infovendas import InfoVenda
import models.vendas_model as VendasModel

TYPE = {'remove': 0, 'info': 1}


class ListaVendas(QWidget):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("ui/ui_listavendas.ui", self)
        self.parent = parent
        self.configTable()
        self.lista_de_vendas = []

        self.carregaVendas()
        self.nova_venda.clicked.connect(self.novaVenda)


    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        # ajusta a altura das linhas
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                 QHeaderView.Stretch)

        # desabilita a edição dos campos
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(False)

    def novaVenda(self):
        self.parent.display(2)       


    def carregaVendas(self):
        self.lista_de_vendas = VendasModel.getVendas()
        self.tableWidget.setRowCount(0)
        for vendas in self.lista_de_vendas:
            self._addRow(vendas)

    def _addRow(self, item):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        id = QTableWidgetItem(str(item.id))
        id.setTextAlignment(Qt.AlignCenter)
        data = QTableWidgetItem(item.data)
        data.setTextAlignment(Qt.AlignCenter)
        nome = QTableWidgetItem(item.cliente.nome)
        fone = QTableWidgetItem(item.cliente.telefone)
        fone.setTextAlignment(Qt.AlignCenter)
        valor = QTableWidgetItem(str(item.valorTotal()))
        valor.setTextAlignment(Qt.AlignCenter)


        self.tableWidget.setCellWidget(rowCount, 0, MeuBotao(item, self, TYPE['info']))
        self.tableWidget.setItem(rowCount, 1, id)
        self.tableWidget.setItem(rowCount, 2, data)
        self.tableWidget.setItem(rowCount, 3, nome)
        self.tableWidget.setItem(rowCount, 4, fone)
        self.tableWidget.setItem(rowCount, 5, valor)
        self.tableWidget.setCellWidget(rowCount, 6, MeuBotao(item, self, TYPE['remove']))


class MeuBotao(QWidget):
    def __init__(self, venda, parent, type):
        super(MeuBotao, self).__init__()
        self.venda = venda
        self.parent = parent

        self.w = None
        self.btn = QPushButton(self)
        self.btn.setText("")
        
        if type == TYPE['remove']:
            self.typeDelete()
        else:
            self.typeInfo()

        self.btn.setStyleSheet('QPushButton {background-color: #00FFFFFF; border:  none}')
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def typeInfo(self):
        self.btn.setIcon(QIcon("icons/info.png"))
        self.btn.clicked.connect(self.maisInfo)
        self.btn.setToolTip("Mais informações sobre a venda")
        self.btn.setIconSize(QSize(20,20))

    def typeDelete(self):
        self.btn.setIcon(QIcon("icons/delete.png"))
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip("Excluir venda")
        self.btn.setIconSize(QSize(20,20))

    def remover(self):
        pass

    def maisInfo(self):
        self.w = InfoVenda(self.venda)
        self.w.show()


