import random
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(random.randint(0, 9))
    matriz.append(fila)
print("Matriz hecha:")
for fila in matriz:
    print(fila)
buscado = int(input("Ingrese el valor que desea buscar en la matriz: "))
encontrado = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == buscado:
            print(f"El valor {buscado} se encontro en la Fila {i}, Columna {j}")
            encontrado = True
if not encontrado:
    print("Elemento no encontrado")