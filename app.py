from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    resultado = {}
    consumo = request.args.get('consumo')
    distancia = request.args.get('distancia')
    try:
        valGasolina = json.loads(open('gasolinaPreco.json','r').readlines()[0])
        if consumo and distancia:
            consumo = int(consumo)
            distancia = int(distancia)
            total_viagem = 0
    except ValueError:
        pass
    
    return render_template('index.html', resultado = resultado)