from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import models.vendas_model as VendasModel

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
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        #self.tableWidget.clicked.connect(self.on_click)

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
        id_cliente = QTableWidgetItem(str(item.cliente.id))
        cliente = QTableWidgetItem(item.cliente.nome)
        #produtos = QTableWidgetItem(venda.lista_de_itens)
        #qtd = QTableWidgetItem(str(item.quantidade))
        #valor_unit = QTableWidgetItem(item.getValorUnitario())
        #valor_total = QTableWidgetItem(item.getValorTotal)
        data = QTableWidgetItem(item.data)
        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, id_cliente)
        self.tableWidget.setItem(rowCount, 2, cliente)
        #self.tableWidget.setItem(rowCount, 3, qtd)
        #self.tableWidget.setItem(rowCount, 3, valor_unit)
        #self.tableWidget.setItem(rowCount, 4, valor_total)
        self.tableWidget.setItem(rowCount, 5, data)



        #rowCount = self.tableWidget.rowCount()
        #self.tableWidget.insertRow(rowCount)

        #print(len(self.lista_de_vendas))