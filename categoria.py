import sqlite3


def cadastrar_categoria():
    id = int(input("Digite o Id da categoria: "))
    nome = input("Digite o nome da categoria: ")

    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = 'insert into categoria (id, nome) values (?, ?)'
    valores = [id, nome]
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nCategoria cadastrada com sucesso!\n")
    conexao.close()


def listar_categoria():
    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = 'select id, nome from categoria'
    resultados = cursor.execute(sql)
    for resultado in resultados:
        print(resultado[0], resultado[1])
    conexao.close()


def atualizar_categoria():
    id = int(input("Digite o Id da Categoria: "))
    nome = input("Informe o novo nome da categoria: ")
    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = f'update categoria set nome = ? where id = {id}'
    valores = [nome]
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nCategoria atualizada com sucesso!\n")
    conexao.close()


def excluir_categoria():
    id = int(input("Digite o Id da Categoria: "))
    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = 'delete from categoria where id = ?'
    valores = [id]
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nCategoria excluida com sucesso!\n")
    conexao.close()
