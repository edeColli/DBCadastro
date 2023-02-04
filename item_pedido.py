import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

sql = '''
  create table item_pedido(
    id int not null,
    pedido_id int not null,
    produto_id int not null,
    quantidade int not null,
    preco real not null,
    primary key (id),
    foreign key (pedido_id) references pedido(id),
    foreign key (produto_id) references produto(id)
  )
  '''

cursor.execute(sql)
conexao.commit()
conexao.close()