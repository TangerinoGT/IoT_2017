from __future__ import division
import threading
import time
from sensores import *
from db_sqlite import *



class thread_Temperatura(threading.Thread):
    ''' Exemplo de imprementacao de uma classe para uso concorrente '''
    def __init__(self, sensor_id, frequencia):
        threading.Thread.__init__(self)
        self.sensor_id = sensor_id
        self.frequencia = frequencia
        self.executando = False

    def run(self):
        self.executando = True
        print 'Iniciando Thread ', self.sensor_id
        while self.executando:
            _,temperatura = get_pot()
            adiciona_dado_sensores(temperatura, temperatura, 'giovana')
            print self.sensor_id, self.executando, str(temperatura)
            time.sleep(1.0/self.frequencia)

    def parar(self):
        print 'parando thread', self.sensor_id
        self.executando = False
