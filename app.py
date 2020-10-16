import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
	anterior = 0
	proximo = 0
	lista = []

	while(proximo < 1000000000000000000003):
		lista.append(proximo)
		proximo = proximo + anterior
		anterior = proximo - anterior
		if(proximo == 0):
			proximo = proximo + 1

	print(lista)
	print("Foram printados",len(lista),"numerais")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



