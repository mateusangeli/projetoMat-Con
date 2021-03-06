# IMPORTA A CLASSE PRODUTO
from utils.produto import Produto
import models.database as db

# PEGA TODOS OS Produto DO BANCO DE DADOS
def getProdutos():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos;")
    lista_Produto = []
    for l in cursor.fetchall():
        id = l[0]
        nome = l[1]
        marca = l[2]
        descricao = l[3]
        precocompra = l[4]
        precovenda = l[5]
        quantidade = l[6]
        novoProduto = Produto(id, nome, marca, descricao, precocompra, precovenda, quantidade)
        lista_Produto.append(novoProduto)
    conn.close()
    return lista_Produto

def getProduto(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Produtos WHERE ID = ?;"""
    cursor.execute(sql, [id])
    l = cursor.fetchall()[0]
    id = l[0]
    nome = l[1]
    marca = l[2]
    descricao = l[3] 
    precocompra = l[4]
    precovenda = l[5]
    quantidade = l[6]
    novoProduto = Produto(id, nome, marca, descricao, precocompra, precovenda, quantidade)
    conn.close()
    return novoProduto

def addProduto(produto):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Produtos (nome, marca, descricao, precocompra, precovenda, quantidade) VALUES (?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql,[produto.nomeP, produto.marca, produto.descricao, produto.precocompra, produto.precovenda, produto.quantidade])
    conn.commit()
    conn.close()

def editProduto(produto):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE Produtos SET nome = ?, marca = ?, descricao = ?, precocompra = ?, precovenda = ?, quantidade = ? WHERE id = ?"""
    cursor.execute(sql,[produto.nomeP, produto.marca, produto.descricao, produto.precocompra, produto.precovenda, produto.quantidade, produto.id])
    conn.commit()
    conn.close()

def delProduto(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """ DELETE FROM Produtos WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()