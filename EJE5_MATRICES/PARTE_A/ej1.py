matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append("-")
        matriz.append(fila)

while True:
    for i in range(5):
        print(matriz[i])
        fila = int(input("Ingrese el numero de la fila: "))
        columna = int(input("Ingrese el numero de la columna: "))
        if fila >= 1 and fila <= 5 and columna >= 1 and columna <= 5:
            matriz[fila - 1][columna - 1] = "X"
        else:
            print("¡ERROR!")


¿Qué es una matriz? Una matriz es una listas de listas
¿Cómo se organizan las matrices? Las matrices se organizan en filas y columnas
¿Cómo puedo acceder a una fila entera de una matriz? A traves del indice 
¿Cómo puedo acceder a un elemento de una matriz? Indicando primero la fila, y despues la columna del elemnto
Desarrolle verbalmente cómo implementó la Inteligencia Artificial la solución pedida. 
Primero necesitamos una matriz de 5 filas y 5 columnas, para crearlas usamos 2 for. El primero para las filas y el segundo crea los 5 elementos de cada fila.
Despues agregamos cada fila a la matriz, luego ponemos while True (para que siempre lo haga, osea siempre es verdaddera)
imprimimos la matriz entera, le pedimos al usuario que cargue que fila y columna desea.
Hacemos como tipo validación para que si llega a poner un numero fuera del rango le escriba ERROR.
