import sqlite3

# conecta ao banco de dados (ou cria se não existir)
conn = sqlite3.connect('my_db_sqlite.db')

# cria um cursor
cursor = conn.cursor()

# exclui a tabela
# cursor.execute("DROP TABLE stocks")

# # cria a tabela
# cursor.execute('''CREATE TABLE stocks (id INTEGER PRIMARY KEY AUTOINCREMENT, name_product TEXT, symbol TEXT UNIQUE, price FLOAT)''')
# cursor.execute('''CREATE TABLE stocks (name_product TEXT, symbol TEXT PRIMARY KEY, price FLOAT)''')

# # insere alguns dados
# cursor.execute("INSERT INTO stocks VALUES (1, 'CSN MINERACAO', 'CMIN3', 2.53)")
# cursor.execute("INSERT INTO stocks VALUES (2, 'ITAU', 'ITUB4', 26.02)")
# cursor.execute("INSERT INTO stocks VALUES (3, 'VALE', 'VALE3', 20.50)")
# cursor.execute("INSERT INTO stocks VALUES (4, 'MAXI RENDA', 'MXRF11', 10.19)")

# cursor.execute("INSERT INTO stocks VALUES ('CSN MINERACAO', 'CMIN3', 2.53)")
# cursor.execute("INSERT INTO stocks VALUES ('ITAU', 'ITUB4', 26.02)")
# cursor.execute("INSERT INTO stocks VALUES ('VALE', 'VALE3', 20.50)")
# cursor.execute("INSERT INTO stocks VALUES ('MAXI RENDA', 'MXRF11', 10.19)")

# cursor.execute("SELECT * FROM stocks")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# salva as alterações
conn.commit()

# fecha a conexão
conn.close()
