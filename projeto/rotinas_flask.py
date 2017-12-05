from flask import Flask, render_template, jsonify
# import fake_sensores as sensores
import db_sqlite
import sensores
import indicadores

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/casa')
def casa_rota():
    return render_template('casa.html')

@app.route('/sensores')
def sensores_rota():
    return render_template('sensores.html')

@app.route('/atuadores')
def atuadores():
    return render_template('atuadores.html')

@app.route('/graficos')
def graficos():
    print 'antes'
    valores_pot = db_sqlite.db_retorna_dados_by_collum('Potenciometro')
    valores_temp = db_sqlite.db_retorna_dados_by_collum('Temperatura')
    print 'depois'
    return render_template('graficos.html', valores_pot=valores_pot, valores_temp=valores_temp)

@app.route('/led_vm/<valor>')
def led_vm(valor):
    valor = int(valor)
    if valor == 1:
        cor = 'vermelho'
    elif valor == 0:
        cor = 'cinza'
    indicadores.escreve_lcd_cor('luz da sala!', str(valor), cor)
    indicadores.led_red(valor)

@app.route('/led_az/<valor>')
def led_az(valor):
    valor = int(valor)
    if valor == 1:
        cor = 'azul'
    elif valor == 0:
        cor = 'cinza'
    indicadores.escreve_lcd_cor('luz do quarto!', str(valor), cor)
    indicadores.led_blue(valor)

@app.route('/led_vd/<valor>')
def led_vd(valor):
    valor = int(valor)
    if valor == 1:
        cor = 'verde'
    elif valor == 0:
        cor = 'cinza'
    indicadores.escreve_lcd_cor('Ar condicionado!', str(valor), cor)
    indicadores.led_green(valor)

    # if valor == 1:
    #     indicadores.led_red(True)
    #     # sensores.liga_rele()
    # elif valor == 0:
    #     indicadores.led_red(False)
    #     # sensores.desliga_rele()
    # else:
    #     return ('valor desconhecido', 200)
    # return ('OK', 200)
#
# @app.route('/lcd/<texto>')
# def lcd(texto):
#     texto_linha1, texto_linha2 = texto.split(',')
#     sensores.escreve_lcd(texto_linha1, texto_linha2)
#     return ('OK', 200)
#
# @app.route('/servo/<valor>')
# def servo(valor):
#     valor = int(valor)
#     sensores.move_servo(valor)
#     return ('OK', 200)
#
# @app.route('/update_temperatura')
# def temperatura():
#     t = sensores.leitura_temperatura()
#     return jsonify(t)
#
# @app.route('/update_potenciometro')
# def potenciometro():
#     p = sensores.leitura_pot()
#     return jsonify(p)
