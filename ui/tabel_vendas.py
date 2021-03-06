from utils.item_venda import ItemVenda
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QComboBox

class TebelaItens():
    def __init__(self,tableWidget, parent):
        self.tableWidget = tableWidget
        self.parent = parent

        self.itemAtual = None
        self.listaItens = []

        self.configTable()
        self.tableWidget.setRowCount(0)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.clicked.connect(self.on_click)


    def on_click(self):
        selected_row = self.tableWidget.currentRow()
        self.itemAtual = self.listaItens[selected_row]
        self.parent.btn_remover_item.setEnabled(True)


    def _addRow(self,item):
        self.listaItens.append(item)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        qtd = QTableWidgetItem(str(item.quantidade))
        nome_produto = QTableWidgetItem(item.getNomeProduto())
        uni = QTableWidgetItem(str(item.getValorUnitario()))
        valor = QTableWidgetItem(str(item.getValor()))
        self.tableWidget.setItem(rowCount,0,qtd)
        self.tableWidget.setItem(rowCount,1,nome_produto)
        self.tableWidget.setItem(rowCount,2,uni)
        self.tableWidget.setItem(rowCount,3,valor)
        self.calculaValorTotal()

    def limparItens(self):
        self.tableWidget.setRowCount(0)
        self.itemAtual = None
        self.listaItens = []
        self.parent.btn_remover_item.setEnabled(False)
        self.parent.btn_limpar_itens.setEnabled(False)

    def limparSelecionado(self):
        self.listaItens.remove(self.itemAtual)
        novaLista = self.listaItens            
        
        self.limparItens()
        self.parent.btn_limpar_itens.setEnabled(True)
        for p in novaLista:
            self._addRow(p)

    def calculaValorTotal(self):
        valorTotal = 0
        desconto = self.parent.desconto.text()
        if desconto == "":
            desconto = "0"       

        for item in self.listaItens:
            valorTotal += (float(item.getValor()))
        desconto = float(desconto)
        if desconto < valorTotal:
            valorTotal = valorTotal - desconto

        desconto2 = 0
        combo = self.parent.combo_pagamento.currentText()
        if combo == "Dinheiro":
            desconto2 = valorTotal * 0.1
        elif combo == "Cart??o de d??bito":
            desconto2 = valorTotal * 0.05

        valorTotal = valorTotal - desconto2
      

        self.parent.valortotal.setText("%.2f" % valorTotal)


        


        
