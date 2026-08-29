matriz = [
    [1, 2, 3],
    [7, 18, 11],
    [12, 4, 19]
]
cont = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        num = matriz[i][j]
        if num > 10:
            print("El número", num, "en la fila", i, "y columna", j, "es mayor a 10")
            cont=cont+1
print("La cantidad de numeros mayores a 10 fueron: " ,cont)
