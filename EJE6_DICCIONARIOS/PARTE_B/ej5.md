# Diccionarios y contadores 2

A partir del ejercicio 4, realizar las siguientes modificaciones:

Los monos van a incorporar algunos cambios a su manejador de frutas para que el identificador les diga si la fruta en cuestión está verde, madura o vieja. Como quieren añadir esta característica diréctamente a la ID de la fruta en cuestión, incorporaron un sistema que hace corresponder los números al estado de la fruta.

Para aplicar esto, hicieron lo siguiente:

Para empezar, en vez de establecer un ID que va de 1 en 1, establecieron un ID que va de 100 en 100 de la siguiente forma:

ANTES:
```
frutas = {
    1: Banana,
    2: Manzana,
    3: Pera,
    4: Manzana
    # ...
}
```
AHORA: 
```
frutas = {
    100: Banana,
    200: Manzana,
    300: Pera,
    400: Manzana
}
```

De esta forma, la primera cifra del número del identificador (el 1 del 100, el 2 del 200, el 3 del 300...) identifica el número que corresponde a la fruta.

Luego, hicieron que la última cifra corresponda al estado de la fruta de la siguiente forma:
1: Madura
2: Verde
3: Vieja

Entonces, ahora solo viendo el identificador se puede saber si la fruta en cuestión está vieja, madura o verde.
Suponiendo que la banana estaba madura, la primera manzana estaba verde, la pera estaba vieja y la segunda banana estaba vieja, el diccionario del ejemplo quedaría
```
frutas = {
    101: Banana,
    202: Manzana,
    303: Pera,
    403: Banana
}
```

Se le pide al alumno realizar un sistema de bananas actualizado que pida ingresar una fruta (manzana, pera o banana) y luego indicar qué nivel de madurez tiene (verde, madura o vieja) y se vea reflejado a través del ID con las reglas ya descritas.