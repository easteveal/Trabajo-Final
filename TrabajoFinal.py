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
			pass
		elif op == 5: # BINGO!!!
			pass
		elif op == 7:
			pass
		elif op == 8:
			pass