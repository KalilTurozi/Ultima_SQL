import sqlite3
conexao = sqlite3.connect('ex_py_ultima')
cursor = conexao.cursor()

print('-='*15,'INSIRA SEUS EXERCICIOS SEMANAIS!','-='*15)

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
print('DADOS INSERIDOS COM SUCESSO!')
conexao.close()