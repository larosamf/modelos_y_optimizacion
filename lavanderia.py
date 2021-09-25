FILE_NAME = "primer_problema.txt"
FILE_RESULTADO = "resultado.txt"


def lavanderia():
	restricciones = {}
	tiempos_lavado = {}
	cantidad_prendas = 20
	prendas_ordenadas_por_tiempo = []
	resultado_lavados = []

	for prenda in range(cantidad_prendas):
		restricciones[prenda+1] = []

	with open(FILE_NAME, 'r') as f:
		for line in f.readlines():
			if line[0] == 'e':
				line = line.split()
				restricciones[int(line[1])].append(int(line[2]))
			elif line[0] == 'n':
				line = line.split()
				tiempos_lavado[int(line[1])] = int(line[2])
				prendas_ordenadas_por_tiempo.append(int(line[1]))

	prendas_ordenadas_por_tiempo = sorted(prendas_ordenadas_por_tiempo, key=lambda x : int(tiempos_lavado[x]))

	numero_lavado = 1
	posicion_segunda_prenda = -2
	while prendas_ordenadas_por_tiempo != []:
		prenda = prendas_ordenadas_por_tiempo[-1]
		segunda_mayor = prendas_ordenadas_por_tiempo[posicion_segunda_prenda]
		
		son_compatible = not (segunda_mayor in restricciones[prenda])
		
		if son_compatible:
			resultado_lavados.append([prenda, numero_lavado])
			resultado_lavados.append([segunda_mayor, numero_lavado])
			
			prendas_ordenadas_por_tiempo.remove(prenda)
			prendas_ordenadas_por_tiempo.remove(segunda_mayor)

			numero_lavado += 1
			posicion_segunda_prenda = -2
		else:
			posicion_segunda_prenda -= 1

	guardar_resultado(resultado_lavados)


def guardar_resultado(lavados):
	file = open(FILE_RESULTADO, "w")
	for lavado in lavados:
		file.write("{} {}\n".format(lavado[0],lavado[1]))

	file.close()

lavanderia()