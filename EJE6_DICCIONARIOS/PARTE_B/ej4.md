# Diccionarios y contadores

Los monos tienen un depósito de frutas. En el sistema informático que están haciendo, las frutas se encuentran en un diccionario, pero cada fruta tiene un número identificador que va incrementando en +1 con cada fruta añadida. 

Crear un sistema con un diccionario "depósito de frutas", de la siguiente forma:
```
frutas = {
    # Vacío al principio
}
```
Y mostrar 3 opciones:

1. Añadir una banana
2. Añadir una pera
3. Añadir una manzana

Cada vez que se añade una fruta, debe salir con su identificador empezando en uno y así sumando uno por cada fruta que haya.

Ejemplo:

Si el usuario ingresa: 1, 1, 2, 3, 2, 3

El diccionario debe quedar:
frutas = {
    1: Banana,
    2: Banana,
    3: Pera,
    4: Manzana,
    5: Pera,
    6: Manzana
}
Imprimir todo el diccionario con claves y valores.
