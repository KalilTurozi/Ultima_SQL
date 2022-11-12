import sqlite3
conexao = sqlite3.connect('ex_py_ultima')
cursor = conexao.cursor()


sql_criar = '''
CREATE TABLE faxina (
    semana INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    segunda TEXT(50),
    terca TEXT(50),
    quarta TEXT(50),
    quinta TEXT(50),
    sexta TEXT(50),
    concluida TEX(50)
)
'''
cursor.execute(sql_criar)
conexao.commit()
conexao.close()