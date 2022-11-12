import sqlite3
conexao = sqlite3.connect('ex_py_ultima')
cursor = conexao.cursor()

sql = '''
SELECT * FROM faxina WHERE semana = 2
'''

consulta = cursor.execute(sql)

for resultado in consulta:
    print(resultado)
