personas = {}

while True:
    print("BIENVENIDO AL MENU")
    print("1. Cargar datos")
    print("2. Buscar por DNI")
    print("3. Buscar por nombre")
    print("4. Terminar")
    
    opcion = int(input("Elija una opción: "))
    
    if opcion == 1:
        dni = int(input("Ingrese el DNI: "))
        nombre = input("Ingrese el nombre: ")
        personas[dni] = nombre
        print("Persona cargada")
        
    elif opcion == 2:
        try:
            dni_a_buscar = int(input("Ingrese el DNI: "))
            encontrado = False
        
            for key in personas.keys():
                if key == dni_a_buscar:
                    print(f"El DNI {key} le pertenece a {personas[key]}")
                    encontrado = True
                    break
                
        except ValueError:
            print("¡ERROR!: El DNI no es válido")
            
    elif opcion == 3:
        try:
            nombre_buscar = input("Ingrese el nombre: ")
            encontrado = False
        
            for key in personas.keys():
                if personas[key] == nombre_buscar:
                    print(f"El nombre {nombre_buscar} le pertenece al dni: {key}")
                    encontrado = True
                    break
                
        except ValueError:
            print("!ERROR¡: El nombre no es válido")
                
    elif opcion == 4:
        print("PROGRAMA FINALIZADO")
        break
    else:
        print("Ingrese una opción válida")