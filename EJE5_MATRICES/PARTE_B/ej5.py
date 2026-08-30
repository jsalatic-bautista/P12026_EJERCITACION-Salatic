import random
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        num = random.randint(0,9)
        fila.append(num)
    matriz.append(fila)
for filas in matriz:
    print("La matriz queda asi: ")
    print(fila)

transpuesta = []
for i in range(5):
    fila_transpuesta = []
    for j in range(5):
     fila_transpuesta.append(matriz[j][i])
    transpuesta.append(fila_transpuesta)
print("La matriz queda: ")
for fila in transpuesta:
    print(fila)