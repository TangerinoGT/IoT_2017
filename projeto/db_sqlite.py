# -*- coding: latin-1 -*-
import sqlite3
import datetime
import time

def db_cria_tabela_domotica():
    try:
    	conect = sqlite3.connect('site.db')
    	cursor = conect.cursor()
    	cursor.execute('''CREATE TABLE IF NOT EXISTS domotica
    	(id INTEGER PRIMARY KEY,
        tipo_sensor TEXT,
        valor REAL,
        unidade TEXT,
        tempo TIMESTAMP DEFAULT (DATETIME('now')))''')
    	conect.commit()
    	conect.close()
        print 'Criando tabela no banco de dados -site.db-'
    except Exception as e:
        print 'except - db_cria_tabela_domotica', e

def db_retorna_dados_domotica(quantidade=None):
    conect = sqlite3.connect('site.db')
    cursor = conect.cursor()
    if not quantidade:
        cursor.execute('''SELECT * FROM domotica ORDER BY datetime(tempo) ASC''')
    else:
        cursor.execute('''SELECT * FROM domotica ORDER BY datetime(tempo) DESC LIMIT ?''',
                       (quantidade,))
    return cursor.fetchall()

def db_adiciona_dado_domotica(tipo_sensor, valor, unidade):
	try:
		conect     = sqlite3.connect('site.db')
		cursor = conect.cursor()
		tempo  = datetime.datetime.now()
		cursor.execute('''INSERT INTO domotica (tipo_sensor, valor, unidade, tempo)
							VALUES(?,?,?,?)''',(tipo_sensor, valor, unidade, tempo))
		conect.commit()
		conect.close()
		if cursor.rowcount > 0:
			return True
		else:
			return False
	except Exception as e:
		print e
		return False
