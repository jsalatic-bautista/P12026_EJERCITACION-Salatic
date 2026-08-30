import random
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(random.randint(1, 9))
    matriz.append(fila)

print("Matriz hecha: ")
for fila in matriz:
    print(fila)
#uso =1 pq es elemento neutro de la multiplocación
multiplicacion = 1
for i in range(5):
    multiplicacion = multiplicacion * matriz[i][i]
print(f"La multiplicacion de la diagonal principal es: {multiplicacion}")