FILE_NAME = "segundo_problema.txt"
FILE_RESULTADO = "resultado_2.txt"
import random


def lavanderia():
	prendas_sin_asignar, restricciones, tiempos_lavado = ordenar_prendas_ordenadas_y_restricciones()
	print(f"Total de prendas: {len(prendas_sin_asignar)}")

	numero_lavado = 1
	resultado_lavados = {}
	print(f"Prendas: {prendas_sin_asignar}")

	while prendas_sin_asignar != []:
		print(f"Número de lavado: {numero_lavado}")
		print(f"Cantidad de prendas sin asignar: {len(prendas_sin_asignar)}")
		resultado_lavados[numero_lavado] = []
		primera_opcion_lavado = obtener_lavado_a_partir_del_orden_de_tiempos(prendas_sin_asignar, restricciones)
		segunda_opcion_lavado = obtener_lavado_de_a_saltos(prendas_sin_asignar, restricciones)
		tercera_opcion_lavado = obtener_lavado_partiendo_de_random(prendas_sin_asignar, restricciones)
		opcion_final_lavado = []


		#Elijo mejor opción por la cantidad de prendas que se lavarían
		tiempos_1 = obtener_tiempo_de_lavado(primera_opcion_lavado, tiempos_lavado)
		tiempos_2 = obtener_tiempo_de_lavado(segunda_opcion_lavado, tiempos_lavado)
		tiempos_3 = obtener_tiempo_de_lavado(tercera_opcion_lavado, tiempos_lavado)		
		if tiempos_1 > tiempos_2 and tiempos_1 > tiempos_3:
			print("Gana opción 1")
			opcion_final_lavado = primera_opcion_lavado.copy()
		elif tiempos_2 > tiempos_1 and tiempos_2 > tiempos_3:
			print("Gana opción 2")
			opcion_final_lavado = segunda_opcion_lavado.copy()
		else: 
			print("Gana opción 3")
			opcion_final_lavado = tercera_opcion_lavado.copy()


		#Asigno prendas a lavado y las elimino de las no asignadas
		resultado_lavados[numero_lavado] = opcion_final_lavado
		for prenda in opcion_final_lavado:
			prendas_sin_asignar.remove(prenda)

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
	return prendas_ordenadas_por_tiempo, restricciones, tiempos_lavado

def obtener_lavado_a_partir_del_orden_de_tiempos(prendas_sin_asignar, restricciones):
	#Obtengo primera opción de lavado como en la Implementación 1
	lavado = []
	for i in range(-1,-len(prendas_sin_asignar)-1,-1):
		prenda = prendas_sin_asignar[i]

		es_compatible = obtener_compatibilidad_con_prendas_de_lavado(prenda, lavado, restricciones)
		if es_compatible:
			lavado.append(prenda)
	return lavado

def obtener_lavado_de_a_saltos(prendas_sin_asignar, restricciones):
	lavado = []
	#Obtengo segundo opción de lavado tomando primero las prendas en posición impar
	for i in range(-1,-len(prendas_sin_asignar)-1,-2):
		prenda = prendas_sin_asignar[i]

		es_compatible = obtener_compatibilidad_con_prendas_de_lavado(prenda, lavado, restricciones)
		if es_compatible:
			lavado.append(prenda)
		
	#Agrego prendas en posicion par a segunda opción
	for i in range(-2,-len(prendas_sin_asignar)-1,-2):
		prenda = prendas_sin_asignar[i]

		es_compatible = obtener_compatibilidad_con_prendas_de_lavado(prenda, lavado, restricciones)
		if es_compatible:
			lavado.append(prenda)
	return lavado

def obtener_lavado_partiendo_de_random(prendas_sin_asignar, restricciones):
	lavado = [random.choice(prendas_sin_asignar)]
	for i in range(-1,-len(prendas_sin_asignar)-1,-1):
		prenda = prendas_sin_asignar[i]
		if prenda in lavado: continue

		es_compatible = obtener_compatibilidad_con_prendas_de_lavado(prenda, lavado, restricciones)
		if es_compatible:
			lavado.append(prenda)
	return lavado

def obtener_compatibilidad_con_prendas_de_lavado(prenda, otras_prendas, restricciones):
	for x in otras_prendas:
		son_compatible = (not (prenda in restricciones[x])) and (not (x in restricciones[prenda]))
		if not son_compatible: return False
	return True

def obtener_tiempo_de_lavado(lavado, tiempos_lavado):
	suma_tiempos_lavado = 0
	for prenda in lavado:
		suma_tiempos_lavado += tiempos_lavado[prenda]
	return suma_tiempos_lavado


def guardar_resultado(lavados):
	file = open(FILE_RESULTADO, "w")
	for numero_lavado in lavados.keys():
		for prenda in lavados[numero_lavado]:
			file.write(f"{prenda} {numero_lavado}\n")

	file.close()

lavanderia()