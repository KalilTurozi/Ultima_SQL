import sqlite3
conexao = sqlite3.connect('ex_py_ultima')
cursor = conexao.cursor()

sql_criar = '''
CREATE TABLE treinos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    segunda TEXT(50),
    terca TEXT (50),
    quarta TEXT (50),
    quinta TEXT (50),
    sexta TEXT (50)
);
'''

cursor.execute(sql_criar)
conexao.commit()
conexao.close()


segunda = input('DIGITE O TREINO DE SEGUNDA-FEIRA: ')
terca = input('DIGITE O TREINO DE TERÇA-FEIRA: ')
quarta = input('DIGITE O TREINO DE QUARTA-FEIRA: ')
quinta = input('DIGITE O TREINO DE QUINTA-FEIRA: ')
sexta = input('DIGITE O TREINO DE SEXTA-FEIRA: ')


sql_inserir ='''
INSERT INTO treinos (segunda, terca, quarta, quinta, sexta) VALUES (?,?,?,?,?)
'''
valores = [segunda, terca, quarta, quinta, sexta]

cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()