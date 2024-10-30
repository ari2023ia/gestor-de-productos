productos = []

def añadir_producto():
    productos_guardados = { "nombre":"", "precio":"", "cantidad":""}
    print("Introduzca el nombre del producto")
    nombre_del_producto = input()
    productos_guardados["nombre"] = nombre_del_producto
    
    while True:
        print("Por favor introduzca su precio")
        precio_del_producto = input()
        
        if (precio_del_producto.isdecimal()):
            productos_guardados["precio"] = precio_del_producto
            break
        else:
            print("Introduzca el precio usando solamente números")
     
    while True:    
        print("Introduzca la cantidad disponible")
        cantidad_de_producto = input()
        if (cantidad_de_producto.isdecimal()):
            productos_guardados["cantidad"] = cantidad_de_producto
            break
        else:
            print("Introduzca la cantidad usando solamente números")

  
    productos.append(productos_guardados)
    pass

def ver_productos():
    if productos:
        print("\nProductos guardados:")
        for i, producto in enumerate(productos):
            print(f"{i + 1}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("\nNo hay productos registrados.")

def actualizar_producto():
    ver_productos()
    if not productos:
        return

    try:
        indice = int(input("\nSeleccione el número del producto que desea actualizar: ")) - 1
        if 0 <= indice < len(productos):
            print("Introduce los nuevos datos (deja en blanco para no cambiar):")

            nuevo_nombre = input("Nuevo nombre del producto: ")
            if nuevo_nombre:
                productos[indice]["nombre"] = nuevo_nombre

            nuevo_precio = input("Nuevo precio del producto: ")
            if nuevo_precio.isdecimal():
                productos[indice]["precio"] = nuevo_precio
            elif nuevo_precio:
                print("Precio inválido, no se actualizará.")

            nueva_cantidad = input("Nueva cantidad del producto: ")
            if nueva_cantidad.isdecimal():
                productos[indice]["cantidad"] = nueva_cantidad
            elif nueva_cantidad:
                print("Cantidad inválida, no se actualizará.")
                
            print("Producto actualizado correctamente.")
        else:
            print("Número de producto no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def eliminar_producto():
    ver_productos()
    if not productos:
        return

    try:
        indice = int(input("\nSeleccione el número del producto que desea eliminar: ")) - 1
        if 0 <= indice < len(productos):
            productos.pop(indice)
            print("Producto eliminado correctamente.")
        else:
            print("Número de producto no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
    pass

def guardar_datos():
    nombre_archivo = "data.txt"
    
    with open(nombre_archivo, "w") as archivo:

        if productos:
            archivo.write("Productos guardados:\n")
            for i, producto in enumerate(productos):
                archivo.write(f"{i + 1}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}\n")
            print(f"Datos guardados exitosamente en '{nombre_archivo}'.")
        else:
            archivo.write("No hay productos registrados.\n")
            print(f"Archivo '{nombre_archivo}' creado, pero no contiene productos.")
    pass

def cargar_datos():
    nombre_archivo = "data.txt"
    
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()  
            print("\nContenido del archivo:")
            print(contenido) 
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe. No se pueden leer los datos.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos en la base de datos")
        print("6: Ver productos de la base de datos")
        print("7: salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
        elif opcion == '6':
            cargar_datos()
        elif opcion == '7':
            break
        else:
            print("Por favor, selecciona una opción válida.")
            
menu()