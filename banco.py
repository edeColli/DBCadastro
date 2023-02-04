import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

sql = '''
  create table pedido(
    id int not null,
    cliente varchar(100),
    data varchar(10),
    primary key (id)
  )
  '''

cursor.execute(sql)
conexao.commit()
conexao.close()