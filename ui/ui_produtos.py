from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from ui.tabel_produtos import TabelaProdutos
from utils.produto import Produto

class CadProdutos(QWidget):
    def __init__ (self):
        super().__init__()
        uic.loadUi("ui/ui_produtos.ui", self)
        self.table = TabelaProdutos(self)
        self.verticalLayout.addWidget(self.table)
        
        self.produtoAtual = None
        self.setEventos()
    
    def setEventos(self):
        self.b_salvar.clicked.connect(self.salvarProduto)
        self.b_excluir.clicked.connect(self.excluirProduto)
        self.b_limpar.clicked.connect(self.limpaCampos)

    def salvarProduto(self):
        novo = self.getProduto()
        if novo != None:
            if self.produtoAtual == None:
                self.table.add(novo)
            else:
                novo.id = self.produtoAtual.id
                self.table.atualizar(novo)
            self.limpaCampos()
    
    def getProduto(self):
        nomeP = self.nomeP.text()
        marca = self.marca.text()
        descricao = self.descricao.text()
        precocompra = self.precocompra.text()
        precovenda = self.precovenda.text()
        quantidade = self.quantidade.text()
        if((nomeP != "") and (marca != "") and (descricao != "") and (precocompra != "") and (precovenda != "") and (quantidade != "")):
            return Produto(-1, nomeP, marca, descricao, precocompra, precovenda, quantidade)
        return None
            
    def insereInfo(self,produto):
        self.produtoAtual = produto
        self.nomeP.setText(produto.nomeP)
        self.marca.setText(produto.marca)
        self.descricao.setText(produto.descricao)
        self.precocompra.setText(produto.precocompra) 
        self.precovenda.setText(produto.precovenda)
        self.quantidade.setText(produto.quantidade)
        self.b_salvar.setText("Atualizar")
        self.b_excluir.setEnabled(True)

    def excluirProduto(self):
        self.table.excluir(self.produtoAtual)
        self.limpaCampos

    def limpaCampos(self):
        self.nomeP.setText("")
        self.marca.setText("")
        self.descricao.setText("")
        self.precocompra.setText("")
        self.precovenda.setText("")
        self.quantidade.setText("")
        self.b_salvar.setText("Salvar")
        self.b_excluir.setEnabled(False)


