# ENTRADA

# Proceso
import random
r = []
t = []
for i in range(1,81):
    t.append(i)

b = random.choice(t)
r.append(b)
t.remove(b)

while True:
    print("MENU:")
    print("Opcion 1: Registrar datos")
    print("Opcion 2: Empezar a jugar")
    print("Opcion 3: Siguiente giro")
    print("Opcion 4: Mostrar resumen")
    print("Opcion 5: BINGO!!!")
    print("Opcion 6: Reiniciar juego")
    print("Opcion 7: Finalizar juego")
    print("Opción 8: Mostrar pozo ganado")
    op = int(input("Digite la opción que necesite: "))
    if 1<=op<=4:
        break
if op == 1:
    j1 = input("Ingrese su nombre: ")
    j1c = int(input("Ingrese el número de cartillas que posee: "))
    op = int(input("Digite la opción que necesite: "))
elif op == 2:
    print("Empezar el juego:")
    for i in range(15):
        print(random.randint(1,80)) 
elif op == 3:
    print("Siguiente giro:")
    for i in range(15):
        print(random.randint(1,80)) 

elif op == 4:
    print(r)
    op = int(input("Digite la opción que necesite: "))
elif op == 5:
    print("Juego finalizado\nMostrando pozo ganado")
    op = int(input("Digite la opción que necesite: "))
elif op == 6:
    print("Reiniciando el juego...\n..que empiece el juego")
    op = int(input("Digite la opción que necesite: "))
elif op == 7:
    print("Se acabó el juego")
    op = int(input("Digite la opción que necesite: "))
elif op == 8:
    print("Mostrar el pozo")
    op = int(input("Digite la opción que necesite: "))
    print("Avance del proyecto ... faltan cambios")
