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


primos()