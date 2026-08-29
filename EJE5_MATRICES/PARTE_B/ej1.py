matriz = []
fila = int(input("Ingrese la cantidad de filas: "))
columna = int(input("Ingrese la cantidad de columnas: "))
for i in range(fila):
     filas = []
     for j in range(columna):
          filas.append("X")
     matriz.append(filas)
     matriz.append(columna)
print([matriz])