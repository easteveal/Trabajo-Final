# ENTRADA

# Proceso
import random, time
from os import system

MAX_NUM_BINGO = 80
numeros = [i for i in range(1, MAX_NUM_BINGO+1)]
op = 0
mensaje = ""
jugadores = []
descalificados = []
juego_iniciado = False
bingo = False
giros = []
jugador_bingo = 0
tiempo_inicio = False

PRECIO_BINGO = 5

mensajes = {
	"juego_no_iniciado": "El juego aún no ha iniciado.",
	"inicio_juego": "El juego acaba de iniciar!!!",
	"tiempo_iniciado": "El juego a iniciado hace:",
	"jugador_registrado": "Se ha registrado un nuevo jugador: ",
	"nuevo_numero": "Nuevo número: ",
	"resumen_giros": "Resumen visualizado.",
	"num_last_giros_view": 5,
	"separador_resumen_orden_numerico": " | ",
	"separador_resumen_orden_jugadas": " > ",
	"cero_giros": "Aún no se a hecho ningún giro.",
	"en_marcha": "Juego en marcha>",
	"sin_jugadores": "Debe registrar algún jugador",
	"todavia_no_bingo": "Todavía no puede cantar BINGO!",
	"bingo_cantado": "BINGO CANTADO!!!",
	"bingo": "BINGO!!!",
	"reinicio": "BINGO REINICIADO!!!",
	"lista_jugadores": "Lista de jugadores",
	"no_giro_jugador_bingo": "No se puede girar, porque un jugador a cantado bingo."
}

titulo = ""

while True:
	system("cls")
	op = 0
	titulo = ""
	if(len(mensaje)>0):
		titulo = mensaje + "\n"
	if (juego_iniciado):
		titulo += ("\n" if len(titulo) else "") + mensajes["en_marcha"].upper() + " " + str(len(giros)) + " GIROS REALIZADOS" + "\n"
	if(len(titulo)>0):
		print(titulo)
	print("MENU:")
	if not bingo:
		print("Opcion 1: Registrar jugador")
		print("Opcion 2: Empezar a jugar")
		print("Opcion 3: Siguiente giro")
		print("Opcion 4: Mostrar resumen")
		print("Opcion 5: BINGO!!!")

	print("Opcion 6: Reiniciar juego")
	print("Opcion 7: Finalizar juego")

	if not bingo: print("Opción 8: Mostrar pozo actual")

	try:
		op = int(input("Elija una opción >> "))
	except Exception:
		pass
	if (0<=op<=8 and not bingo) or (6<=op<=7):
		if op == 1: # Registrar jugador
			pass
		elif op == 2: # Empezar a jugar
			pass
		elif op == 3: # Siguiente giro
			pass
		elif op == 4: # Mostrar resumen
			if not juego_iniciado:
				mensaje = mensajes["juego_no_iniciado"]
			else:
				if len(giros)>0:
					mensaje = mensajes["resumen_giros"]

					resultado = "RESUMEN DE JUGADAS: " + str(len(giros)) + " GIROS REALIZADOS\n\n"

					CANT_GIROS_FILA_JUGADAS = 10

					filas_orden_jugadas = []
					fila_jugadas = []
					filas_orden_numérico = [[] for i in range(8)]

					giros.reverse()
					for num_giro in giros:
						# orden por jugadas
						valor_en_texto = str(num_giro)
						if len(valor_en_texto)==1: valor_en_texto = "0" + valor_en_texto
						fila_jugadas.append(valor_en_texto)
						if len(fila_jugadas)==CANT_GIROS_FILA_JUGADAS:
							filas_orden_jugadas.append(fila_jugadas.copy())
							fila_jugadas.clear()
						# orden numérico
						rango = int( (num_giro-1) / 10 ) # retorna de 0 al 7 (0 cuando  1 <= num_giro <= 10, 1 cuando  11 <= num_giro <= 20, ..., 7 cuando  71 <= num_giro <= 80)
						filas_orden_numérico[rango].append(valor_en_texto)
					else:
						filas_orden_jugadas.append(fila_jugadas.copy())

					giros.reverse()

					SEPARADOR_INICIAL = "     "

					SEPARADOR_FINAL = "\n"

					resultado += " * Por orden de jugadas (desde la última hacia la primera)\n"
					for fila in filas_orden_jugadas:
						resultado += SEPARADOR_INICIAL + mensajes["separador_resumen_orden_jugadas"].join(fila) + mensajes["separador_resumen_orden_jugadas"] + SEPARADOR_FINAL

					resultado = resultado[:-1*len(mensajes["separador_resumen_orden_jugadas"] + SEPARADOR_FINAL)] + SEPARADOR_FINAL

					num_last_jugadas = int(mensajes["num_last_giros_view"]) if int(mensajes["num_last_giros_view"]) <= CANT_GIROS_FILA_JUGADAS else CANT_GIROS_FILA_JUGADAS
					
					mensaje += " Últimas " + str(mensajes["num_last_giros_view"]) + " jugadas: " + mensajes["separador_resumen_orden_jugadas"].join(filas_orden_jugadas[0][:num_last_jugadas])

					resultado += "\n * Por orden numérico (agrupados de 10 en 10)\n"
					for i in range(len(filas_orden_numérico)):
						if len(filas_orden_numérico[i])>0:
							filas_orden_numérico[i].sort()
							limit_inferior_str = str(10*i+1)
							if i==0: limit_inferior_str = "0"+limit_inferior_str
							resultado += SEPARADOR_INICIAL + "[" + limit_inferior_str + "-" + str(10*(i+1)) + "]: " + mensajes["separador_resumen_orden_numerico"].join(filas_orden_numérico[i]) + SEPARADOR_FINAL
					
					resultado += "\n"
					if (jugador_bingo>0):
						op = 0
						while True:
							system("cls")
							print(resultado)
							print("Opcion 1: Bingo del jugador " + str(jugador_bingo) + ": " + jugadores[jugador_bingo-1][0] + " (" + str(jugadores[jugador_bingo-1][1]) + ")")
							print("Opcion 2: Descalificarlo")
							try:
								op = int(input("Elija una opción >> "))
							except:
								pass
							if 1<=op<=2:
								if op==1:
									bingo = True
									pozo = 0
									for jugador in jugadores:
										pozo += jugador[1]*PRECIO_BINGO
									mensaje = mensajes["bingo"] + " POZO GANADO S/. " + str(pozo) 
								if op==2:
									descalificados.append(jugador_bingo)
									if len(jugadores) == len(descalificados): juego_iniciado = False
									mensaje = "Continuamos, jugador " + str(jugador_bingo) + " descalificado."
									jugador_bingo = 0
								break
					else:
						system("cls")
						print(resultado)
						input("Presione ENTER para continuar  ")
				else:
					mensaje = mensajes["cero_giros"]

		elif op == 5: # BINGO!!!
			pass
		elif op == 7:
			pass
		elif op == 8:
			pass