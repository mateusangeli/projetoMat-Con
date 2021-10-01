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
    sql = """SELECT * FROM Usuarios WHERE usuario = ? AND senha = ?;"""
    cursor.execute(sql, [usuario, senha])
    nova_lista = []
    for s in cursor.fetchall():
        id = s[0]
        nome = s[1]
        usuario = s[2]
        senha = s[3]
        new = Login(id, nome, usuario, senha)
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