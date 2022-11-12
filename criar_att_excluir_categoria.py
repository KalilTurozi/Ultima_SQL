import sqlite3
conexao = sqlite3.connect('ex_py_ultima')
cursor = conexao.cursor()

sql_excluircategoria = '''
DELETE FROM faxina WHERE semana = 3
'''

cursor.execute(sql_excluircategoria)
conexao.commit()
print('DADOS EXCLUIDOS COM  SUCESSO!')
conexao.close()