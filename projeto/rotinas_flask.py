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
    # valores = db_sqlite.retorna_dados_sensores()
    # return render_template('graficos.html', valores=valores)
    return render_template('graficos.html')

@app.route('/led/<valor>')
def led(valor):
    indicadores.escreve_lcd_cor('funciona!', str(valor), 'verde')
    valor = int(valor)
    indicadores.led_red(valor)
    indicadores.led_green(valor)
    # if valor == 1:
    #     indicadores.led_red(True)
    #     # sensores.liga_rele()
    # elif valor == 0:
    #     indicadores.led_red(False)
    #     # sensores.desliga_rele()
    # else:
    #     return ('valor desconhecido', 200)
    return ('OK', 200)
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
