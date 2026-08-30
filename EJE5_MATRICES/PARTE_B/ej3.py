matriz = []
num = int(input("Ingrese un numero para armar la matriz: "))
for i in range(num):
    fila = []
    for j in range(num):
       valor =  int(input(f"Ingrese los numeros para [{i}][{j}]: "))
       fila.append(valor)
    matriz.append(fila)
print("La matriz queda: ")
for fila in matriz:
    print(matriz)
    total = 0
    for i in range(num):
        for j in range(num):
            total = total + matriz[i][j]
    print("La suma de la matriz es de: ", {total})