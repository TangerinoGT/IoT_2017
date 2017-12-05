# -*- coding: latin-1 -*-
'''
Curso IoT 2017 - IFSP Piracicaba
Professor: Gustavo Voltani von Atzingen
alterações: Giovana Tangerino
'''
from wiringx86 import GPIOGalileo as GPIO
from upm import pyupm_jhd1313m1 as lcd

#pinos GPIO
pino_led_red = 8 #D8
pino_led_green = 7 #D7
pino_led_blue =  6 #D6

# numeracao dos pinos conectados aos sensores de acordo com a bibliteca usada
pinos = GPIO(debug=False)
tela = lcd.Jhd1313m1(0, 0x3E, 0x62)

pinos.pinMode(pino_led_red, pinos.OUTPUT);
pinos.pinMode(pino_led_green, pinos.OUTPUT);
pinos.pinMode(pino_led_blue, pinos.OUTPUT);

def escreve_lcd(texto_linha1, texto_linha2):
    tela.clear()
    tela.setCursor(0, 0)
    tela.write(texto_linha1)
    tela.setCursor(1, 0)
    tela.write(texto_linha2)


def escreve_lcd_cor(texto_linha1, texto_linha2, cor):
    tela.clear()
    tela.setCursor(0, 0)
    tela.write(texto_linha1)
    tela.setCursor(1, 0)
    tela.write(texto_linha2)
    # escala RGB
    if cor == 'vermelho':
        tela.setColor(255, 10, 10)
    elif cor == 'verde':
        tela.setColor(10, 255, 100)
    elif cor == 'azul':
        tela.setColor(10, 100, 255)
    elif cor == 'cinza':
        tela.setColor(10, 10, 10)
    else:
        tela.setColor(0, 0, 0)
    # colocar alguma ação de erro quando escreverem a cor errada

def escreve_lcd_RGB(texto_linha1, texto_linha2, R,G,B):
    tela.clear()
    tela.setCursor(0, 0)
    tela.write(texto_linha1)
    tela.setCursor(1, 0)
    tela.write(texto_linha2)
    # escala RGB
    tela.setColor(R, G, B)
    # colocar alguma ação de erro quando escreverem a cor errada

def led_red(comando):
    if comando:
        pinos.digitalWrite(pino_led_red, pinos.HIGH)
    else:
        pinos.digitalWrite(pino_led_red, pinos.LOW)

def led_green(comando):
    if comando:
        pinos.digitalWrite(pino_led_green, pinos.HIGH)
    else:
        pinos.digitalWrite(pino_led_green, pinos.LOW)

def led_blue(comando):
    if comando:
        pinos.digitalWrite(pino_led_blue, pinos.HIGH)
    else:
        pinos.digitalWrite(pino_led_blue, pinos.LOW)
