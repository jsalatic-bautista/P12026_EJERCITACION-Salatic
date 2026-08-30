matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        num = int(input(f"Ingrese el numero para la posicion [{i}][{j}]: "))
        fila.append(num)
    matriz.append(fila)
for i in range(3):
    total = 0
    for j in range(3):
        total = total + matriz[i][j]
    print(f"La suma de la fila [{i}]: {total}")
