
#Productos = [{"nombre": , "precio": ,"cantidad": }]

while True:
    
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")

    opcion = input("Ingrese la opción que desea ejecutar: ")
    
    try:
        opcion = int(opcion) 
    except ValueError:
        print(" Error. Ingrese un número válido segun la opción que desea")

        
    match opcion:
        case 1:
            print("uno")
        case 2:
            print("uno")
        case 3:
            print("uno")
        case 4:
            print("uno")
        case 5:
            print("uno")
        case 6:
            break
        case _:
            print(" Error: Ingrese un número entre 1 y 6 segun la opción que desea")


    