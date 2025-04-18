
def agregar_producto(nombre, precio, cantidad):
    for producto in productos:
        if producto["Nombre"] == nombre:
            producto["Cantidad"] += cantidad
            print("\nProducto ya existente. Se le ha sumado la cantidad que ingresó.")
            return
    producto = {"Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad}
    productos.append(producto)
    print("\nProducto añadido correctamente.")

def consultar_producto(nombre):
    for producto in productos:
        if producto["Nombre"] == nombre:
            print(f"\nNombre: {producto["Nombre"]}")
            print(f"Precio: {producto["Precio"]}")
            print(f"Cantidad: {producto["Cantidad"]}")
            return
    print(f"\nError. El producto "{nombre}" no se encuentra en la lista de productos almacenados.")


productos = []

while True:
    
    print("\n1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")

    while True:
        try:
            opcion = input("\nIngrese la opción que desea ejecutar: ")
            opcion = int(opcion) 
            break
        except ValueError:
            print("\nError. Ingrese un número válido segun la opción que desea")

        
    match opcion:

        case 1:

            while True:
                nombre = input("\nIngrese el nombre del producto: ").strip().lower()
                if nombre == "":
                    print("\nError. El nombre del producto no puede estar vacío.")
                else:
                    break

            while True:
                try:
                    precio = input("\nIngrese el precio del producto: ")
                    precio = float(precio)
                    if precio <= 0:
                        print("\nError. El precio del producto debe ser mayor a 0.")
                    else:
                        break
                except ValueError:
                    print("\nError. El precio del producto debe ser un número.")

            while True:
                try:
                    cantidad = input("\nIngrese la cantidad del producto: ")
                    cantidad = int(cantidad)
                    if cantidad <= 0:
                        print("\nError. La cantidad del producto debe ser mayor a 0.")
                    else:
                        break
                except ValueError:
                    print("\nError. La cantidad del producto debe ser un número entero.")
            
            agregar_producto(nombre, precio, cantidad)

        case 2:
            
            while True:
                nombre = input("\nIngrese el nombre del producto que desea buscar en el inventario: ").strip().lower()
                if nombre == "":
                    print("\nError. El nombre del producto no puede estar vacío.")
                else:
                    break
            
            consultar_producto(nombre)

        case 3:
            print("uno")
        case 4:
            print("uno")
        case 5:
            print(f"\n{productos}")
        case 6:
            break
        case _:
            print("\nError. Ingrese un número entre 1 y 6 segun la opción que desea")


    