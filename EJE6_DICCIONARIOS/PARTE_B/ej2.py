biblioteca = {
    "Ficción": {
        101: "1984",
        102: "Son comos niños"
    },
    "Terror": {
        201: "It",
        202: "El resplandor"
    },
    "Ciencia Ficción": {
        301: "Dune",
        302: "Fundación"
    }
}
while True:
    print("  BIBLIOTECA  ")
    print("1. Agregar libro")
    print("2. Ver todos los libros por género")
    print("3. Buscar libro por ID y género")
    print("4. Salir")
    
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        genero = input("Ingrese el género: ")
        id_libro = int(input("Ingrese el ID del libro: "))
        titulo = input("Ingrese el título del libro: ")

        if genero in biblioteca:
            pass
        else:
            biblioteca[genero] = {}
        
        biblioteca[genero][id_libro] = titulo
        print("Libro agregado")

    elif opcion == 2:
        for genero, libros in biblioteca.items():
            print(f"Género: {genero}")
            for id_libro, titulo in libros.items():
                print(f"  ID: {id_libro}  Título: {titulo}")

    elif opcion == 3:
        genero = input("Ingrese el género: ")
        if genero in biblioteca:
            id_libro = int(input("Ingrese el ID a buscar: "))
            if id_libro in biblioteca[genero]:
                print(f"Título: {biblioteca[genero][id_libro]}")
            else:
                print("ID no encontrado")
        else:
            print("El género no existe")

    elif opcion == 4:
        print("Programa finalizado")
        break
else:
    print("Opción no valida")