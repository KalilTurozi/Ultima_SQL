import sqlite3
conexao = sqlite3.connect('ex_py_ultima')
cursor = conexao.cursor()

sql = '''
SELECT * FROM faxina
'''

seleciona = cursor.execute(sql)

for i in seleciona:
    print(i)