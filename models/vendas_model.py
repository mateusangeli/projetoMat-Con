from utils.cliente import Cliente
from utils.venda import Venda
from utils.item_venda import ItemVenda
import models.database as db
import models.clientes_model as ClienteModel
import models.produtos_model as ProdModel


def addVenda(venda):
    conn = db.connect_db()
    cursor = conn.cursor()

    sql_addVenda = "INSERT INTO Vendas (id_cliente, valor_total, data) VALUES (?, ?, ?)"
    valuesVenda = [venda.cliente.id, venda.valorTotal(), venda.data]
    cursor.execute(sql_addVenda, valuesVenda)
    conn.commit()

    sql_id_venda = "SELECT LAST_INSERT_ROWID() AS id;"
    cursor.execute(sql_id_venda)
    rowID = id_venda = cursor.fetchall()[0]
    id_venda = rowID[0]


    sql_addItens = "INSERT INTO itensVenda(id_venda, id_produto, qtd, valor_unit) VALUES (?, ?, ?, ?)"
    listaItens = venda.getItens()
    for item in listaItens:
        valuesItem = [id_venda, item.produto.id, item.quantidade, item.getValorUnitario()]
        cursor.execute(sql_addItens, valuesItem)
        conn.commit()
    conn.close()

def getVendas():
    conn = db.connect_db()
    cursor = conn.cursor()
    lista_de_vendas = []
    sql = "SELECT * FROM Vendas;"
    cursor.execute(sql)
    for l in cursor.fetchall():
        id_venda = l[0]
        id_cliente = l[1]
        valor_total = l[2]
        data = l[3]


        lista_de_itens = []
        sql_itens = "SELECT * FROM itensVenda WHERE id_venda = ?;"
        valuesItens = [id_venda]
        cursor.execute(sql_itens, valuesItens)
        for i in cursor.fetchall():
            id_produto = i[1]
            qtd = i[2]
            valor_unit = i[3]

            produto = ProdModel.getProduto(id_produto)
            item = ItemVenda(qtd, produto, valor_unit)
            lista_de_itens.append(item)
        cliente = ClienteModel.getCliente(id_cliente)
        venda = Venda(id_venda, cliente, lista_de_itens, valor_total, data)
        lista_de_vendas.append(venda)
    conn.close()
    return lista_de_vendas

'''def delVenda(id_venda):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """DELETE FROM Venda WHERE id_venda = ?"""
    cursor.execute(sql, [id_venda])
    conn.commit()
    conn.close()'''

    #sql = "SELECT v.id, c.nome as cliente, c.telefone, v.valor_total FROM Vendas v, Clientes c WHERE v.id_cliente = c.id"
