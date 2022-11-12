import sqlite3
conexao = sqlite3.connect('ex_py_ultima')
cursor = conexao.cursor()

print('-='*20)

segunda = input('DIGITE A FAXINA DA SEGUNDA-FEIRA: ')
terca = input('DIGITE A FAAXINA DA TERÇA-FEIRA: ')
quarta = input('DIGITE A FAXINA DA QUARTA-FEIRA: ')
quinta = input('DIGITE A FAXINA DA QUINTA-FEIRA: ')
sexta = input('DIGITE A FAXINA DA SEXTA-FEIRA: ')
concluido = input('SUAS TAREFAS FORÃO CONCLUIDA?: ')

sql = '''
INSERT INTO faxina (segunda, terca, quarta, quinta, sexta, concluida)
VALUES (?,?,?,?,?,?)
'''
valores = [segunda, terca, quarta, quinta, sexta, concluido]
cursor.execute(sql, valores)
conexao.commit()
print( 'DADOS INSERIDOS COM SUCESSO!')
conexao.close()