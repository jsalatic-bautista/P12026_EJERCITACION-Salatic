# Pase de un diccionario a otro 2 (diccionarios dentro de diccionarios)

Basado en el sistema anterior, ahora se va a cambiar la disposición de los tripulantes en el barco. Los tripulantes pueden estar en la babor, estribor o proa del barco. 

El diccionario que los contiene ahora debe discriminar en qué parte del barco están, y el trasbordo debe decidir a qué parte del otro barco son llevados.

Ejemplo:

```
barco_a = {
    'proa': {
        10250350: Pepe,
        20202020: Juan,
        30303030: José 
        },
    'babor': {
        15151515: Juan,
        43434343: Sara,
        38383838: Arnaldo
    },
    'estribor': {
        67676767: Hortencio
    }
}
```

Nótese que barco_a es un diccionario que contiene TRES DICCIONARIOS. Se accede a cada uno de estos tres diccionarios a través de las claves 'proa', 'babor' y 'estribor'.