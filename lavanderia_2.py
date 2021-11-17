FILE_NAME = "segundo_problema.txt"
FILE_RESULTADO = "resultado_2.txt"


def lavanderia():
	prendas_sin_asignar, restricciones = ordenar_prendas_ordenadas_y_restricciones()
	print(f"Total de prendas: {len(prendas_sin_asignar)}")

	numero_lavado = 1
	resultado_lavados = {}

	while prendas_sin_asignar != []:
		prendas_ordenadas_por_tiempo = prendas_sin_asignar.copy()
		print(f"Número de lavado: {numero_lavado}")
		print(f"Cantidad de prendas sin asignar: {len(prendas_sin_asignar)}")
		resultado_lavados[numero_lavado] = []
		while prendas_ordenadas_por_tiempo != []:
			prenda = prendas_ordenadas_por_tiempo[-1]

			es_compatible = obtener_compatibilidad_con_prendas_de_lavado(prenda, resultado_lavados[numero_lavado], restricciones)
			if es_compatible:
				resultado_lavados[numero_lavado].append(prenda)
				prendas_sin_asignar.remove(prenda)
			
			prendas_ordenadas_por_tiempo.remove(prenda)
		print(f"Prendas en lavado {numero_lavado}: {resultado_lavados[numero_lavado]}")
		numero_lavado += 1

	guardar_resultado(resultado_lavados)


def ordenar_prendas_ordenadas_y_restricciones():
	restricciones = {}
	tiempos_lavado = {}
	cantidad_prendas = 385
	prendas_ordenadas_por_tiempo = []

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
	return prendas_ordenadas_por_tiempo, restricciones


def obtener_compatibilidad_con_prendas_de_lavado(prenda, otras_prendas, restricciones):
	for x in otras_prendas:
		son_compatible = (not (prenda in restricciones[x])) and (not (x in restricciones[prenda]))
		if not son_compatible: return False
	return True


def guardar_resultado(lavados):
	file = open(FILE_RESULTADO, "w")
	for numero_lavado in lavados.keys():
		for prenda in lavados[numero_lavado]:
			file.write(f"{prenda} {numero_lavado}\n")

	file.close()

lavanderia()