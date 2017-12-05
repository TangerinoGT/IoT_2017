 # -*- coding: latin-1 -*-

import time
from indicadores import *
from sensores import *
from rotinas_flask import *
from rotinas_thread import *

import signal
import psutil
# import process

leitura_temperatura = thread_temperatura('Temperatura', .1)
leitura_potenciometro = thread_potenciometro('Potenciometro', .1)
db_cria_tabela_domotica()

#
# permite matar o processo
def signal_handler(signal, frame):
    for process in psutil.process_iter():                #varre lista de processo da maquina
        if process.cmdline() == ['python', 'principal.py']:   #se encontrar o processo
            print ' '
            print 'Processo: ' + str(process.pid)
            print 'Processo encerrado!'
            process.terminate()                          #pega o processo e termina
signal.signal(signal.SIGINT, signal_handler)             #gera calback por KI caso Ctrl+C

if __name__ == '__main__':

    # leitura_temp = get_temp()
    # print "temperatura: ", leitura_temp
    #
    # leitura_pot5,leitura_pot1023 = get_pot()
    # print "potenciômetro de 0 a 5: ", leitura_pot5
    # print "potenciômetro de 0 a 1023: ", leitura_pot1023
    #
    # escreve_lcd_cor(str(leitura_pot5),str(leitura_pot1023),'vermelho')

    leitura_potenciometro.start()
    leitura_temperatura.start()

    app.run(debug=False, host='0.0.0.0')

    leitura_potenciometro.parar()
    leitura_temperatura.parar()

    # time.sleep(2)
