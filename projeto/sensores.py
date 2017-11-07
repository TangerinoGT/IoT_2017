# -*- coding: latin-1 -*-
'''
Curso IoT 2017 - IFSP Piracicaba
Professor: Gustavo Voltani von Atzingen
alterações: Giovana Tangerino
'''
from wiringx86 import GPIOGalileo as GPIO
from upm import pyupm_temperature as upm

# numeracao dos pinos conectados aos sensores de acordo com a bibliteca usada
pino_pot = 14 #Gbiblioteca PIOGalileo: A0=14, A1=15
pino_sensor_temperatura = 1 #biblioteca pyupm_temperature: A0=0, A1=1

pinos = GPIO(debug=False)
pinos.pinMode(pino_pot, pinos.ANALOG_INPUT)
temperatura = upm.Temperature(pino_sensor_temperatura)

def get_temp():
    return temperatura.value()

def get_pot():
    resultado_adc = pinos.analogRead(pino_pot)
    voltagem = resultado_adc*5.0/1023.0
    return voltagem, resultado_adc
