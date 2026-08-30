num = int(input("Ingrese el tamaño N para las matrices: "))
matriz = []

for i in range(num):
    fila = []
    for j in range(num):
        valor = int(input(f"Matriz 1 - Ingrese el numero para [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

matriz1 = []
for i in range(num):
    fila1 = []
    for j in range(num):
        valor1 = int(input(f"Matriz 2 - Ingrese el numero para [{i}][{j}]: "))
        fila1.append(valor1)
    matriz1.append(fila1)

matrizresultado = []
for i in range(num):
    filasuma = []
    for j in range(num):
        sumaposicion = matriz[i][j] + matriz1[i][j]
        filasuma.append(sumaposicion)
    matrizresultado.append(filasuma)

print("\nMatriz Resultante:")
for fila in matrizresultado:
    print(fila)