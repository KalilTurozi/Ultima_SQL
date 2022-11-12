import sqlite3
con = sqlite3.connect('database\clinica.sqlite')

cur = con.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS paciente(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100) NOT NULL,
    sobrenome TEXT(100) NOT NULL,
    id_convenio INTEGER NOT NULL
);
'''
cur.execute(sql)
con.commit()

sql_drop = 'DROP TABLE IF EXISTS paciente;'
cur.execute(sql_drop)
con.commit()
con.close()