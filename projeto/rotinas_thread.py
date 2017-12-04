from __future__ import division
import threading
import time
from sensores import *
from db_sqlite import *



class thread_temperatura(threading.Thread):
    ''' Exemplo de imprementacao de uma classe para uso concorrente '''
    def __init__(self, tipo_sensor, frequencia):
        threading.Thread.__init__(self)
        self.tipo_sensor = tipo_sensor
        self.frequencia = frequencia
        self.executando = False

    def run(self):
        self.executando = True
        print 'Iniciando Thread ', self.tipo_sensor
        while self.executando:
            temperatura = get_temp()
            db_adiciona_dado_domotica('Temperatura', temperatura, 'Celsius')
            print self.tipo_sensor, self.executando, str(temperatura)
            time.sleep(1.0/self.frequencia)

    def parar(self):
        print 'parando thread', self.tipo_sensor
        self.executando = False

class thread_potenciometro(threading.Thread):
    ''' Exemplo de imprementacao de uma classe para uso concorrente '''
    def __init__(self, tipo_sensor, frequencia):
        threading.Thread.__init__(self)
        self.tipo_sensor = tipo_sensor
        self.frequencia = frequencia
        self.executando = False

    def run(self):
        self.executando = True
        print 'Iniciando Thread: ', self.tipo_sensor
        while self.executando:
            _,valor = get_pot()
            db_adiciona_dado_domotica('Potenciometro', valor, '0-1023')
            print self.tipo_sensor, str(valor)
            time.sleep(1.0/self.frequencia)

    def parar(self):
        print 'parando thread', self.tipo_sensor
        self.executando = False
