import sqlite3


def cadastrar_produto():
    id = int(input("Digite o Id do produto: "))
    nome = input("Digite o nome do produto: ")
    id_categoria = int(input("Digite o Id da categoria: "))
    descricao = input("Digite a descrição do produto: ")

    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = 'insert into produto (id, nome, id_categoria, descricao) values (?, ?, ?, ?)'
    valores = [id, nome, id_categoria, descricao]
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nProduto cadastrado com sucesso!\n")
    conexao.close()


def listar_produto():
    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = 'select * from produto'
    resultados = cursor.execute(sql)
    for resultado in resultados:
        print(resultado)
    conexao.close()


def atualizar_produto():
    id = int(input("Digite o Id do Produto: "))
    nome = input("Informe o novo nome do produto: ")
    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = f'update produto set nome = ? where id = {id}'
    valores = [nome]
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nProduto atualizado com sucesso!\n")
    conexao.close()


def excluir_produto():
    id = int(input("Digite o Id do Produto: "))
    conexao = sqlite3.connect('db.sqlite3')
    cursor = conexao.cursor()
    sql = 'delete from produto where id = ?'
    valores = [id]
    cursor.execute(sql, valores)
    conexao.commit()
    print("\nProduto excluido com sucesso!\n")
    conexao.close()
