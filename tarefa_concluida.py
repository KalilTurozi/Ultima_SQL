import sqlite3

conexao = sqlite3.connect ('ex_py_ultima')
cursor = conexao.cursor()


sql = '''
ATUALIZAÇÃO faxina SET concluida = 'CONCLUÍDO' ONDE semana = 1
'''
cursor.execute(sql)
conexao.commit()
conexao.close()