from utils.login import Login
import models.database as db


def getLogins():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Usuarios;""")
    lista_usuarios = []
    for u in cursor.fetchall():
        id = u[0]
        nome = u[1]
        usuario = u[2]
        senha = u[3]
        novoUsuario = Login(id, nome, usuario, senha)
        lista_usuarios.append(novoUsuario)
    conn.close()
    return lista_usuarios

def getLogin(usuario, senha):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT nome, usuario, senha FROM Usuarios WHERE usuario = ? AND senha = ?;"""
    conn.execute(sql, ['adm', '123'])
    nova_lista = []
    print(cursor.fetchall())
    for s in cursor.fetchall():
        user = s[1]
        password = s[2]
        new = Login(user, password)
        nova_lista.append(new)
    conn.close()
    return nova_lista



def addLogin(login):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Usuarios (nome, usuario, senha) VALUES (?, ?, ?);"""
    cursor.execute(sql,[login.nome, login.usuario, login.senha])
    conn.commit()
    conn.close()

def delLogin(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """DELETE * FROM Usuarios WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()