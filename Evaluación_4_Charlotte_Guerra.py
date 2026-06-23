#Lista inicial.

productos=[]

#Funciones de validación.

def validar_producto(nombre):
    return nombre.strip()

def validar_stock(stock):
    return stock >= 0

def validar_precio(precio):
    return precio > 0

#Funcion del menú

def mostrar_menu():
    print("\n==========MENÚ PRINCIPAL==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")

#Funcion leer opción y validar.

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error. Debe ingresar un númer válido entre 1 - 6.\nIntente nuevamente.")
        except ValueError:
            print("Error. Debes ingresar una opción válida...")

#Función para agregar producto y validaciones correspondientes.

def agregar_producto(lista):

    nombre=str(input("Ingrese el nombre del producto a registrar: "))
    
    if not validar_producto(nombre):
        print("Error. El nombre del producto no debe estar vacío...")
        return
    
    try:
        stock=int(input("Ingrese la cantidad de stock del producto: "))
        if not validar_stock(stock):
            print("Error. Debes ingresar un número válido...")
            return
    except ValueError:
        print("Error. Debes ingresar un valor númerico válido.")

    try:
        precio=float(input("Ingrese el valor del producto (En decimales): "))
        if not validar_precio(precio):
            print("Error. El valor debe ser un número mayor a cero...")
            return
    except ValueError:
        print("Error. Debes ingresar un valor decimal válido.")

    inventario={"nombre":nombre,
                "stock":stock,
                "precio":precio,
                "estado":False
                }
    
    lista.append(inventario)
    print("¡Inventario registrado exitosamente!")

#Función para realizar busqueda de producto en lista.

def buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"]==nombre:
            return i
        return -1

#Función para eliminar producto de la lista inventario.

def eliminar_producto(lista):
    nombre=str(input("Ingrese el nombre del producto que desea eliminar: "))
    posicion=buscar_producto(lista, nombre)

    if posicion != -1:
        lista.pop(posicion)
        print("El producto ha sido eliminado del inventario.")
    else:
        print(f"El producto {nombre} no se encuentra registrado.")

#Función para actualizar disponibilidad en inventario.

def actualizar_disponibilidad(lista):
    for inventario in lista:
        if inventario["stock"] > 0:
            inventario["disponible"] = True
        else:
            inventario["disponible"] = False
    print("Los datos del inventario han sido actualizados exitosamente.")

#Función para mostrar productos.

def mostrar_inventario(lista):
    actualizar_disponibilidad(lista)

    if len(lista) == 0:
        print("No existen datos de inventario registrados en sistema...")
        return
    
    print("\n==========LISTA INVENTARIO DE PRODUCTOS==========")
    for inventario in lista:
        estado = "DISPONIBLE" if inventario["disponible"] else "SIN STOCK"

        print(f"nombre: {inventario["nombre"]}")
        print(f"cantidad: {inventario["stock"]}")
        print(f"precio: {inventario["precio"]}")
        print(f"estado: {estado}")
        print(f"========================================================")

#Ejecutar menú y llamar a funciones.

while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion == 1:
        agregar_producto(productos)

    elif opcion == 2:
        nombre=str(input("Ingrese el nombre del producto a buscar: "))
        posicion = buscar_producto(productos, nombre)
        if posicion != -1:
            inventario=productos[posicion]
            print(f"\nProducto encontrado en el índice {posicion+1}: ")
            print("==========DETALLE DE INVENTARIO==========")
            estado = "DISPONIBLE" if inventario["disponible"] else "SIN STOCK"
            print(f"nombre: {inventario["nombre"]}")
            print(f"cantidad: {inventario["stock"]}")
            print(f"precio: {inventario["precio"]}")
            print(f"estado: {estado}")
            print(f"========================================")
        else:
            print("Producto no encontrado en inventario...\nIntente nuevamente.")

    elif opcion == 3:
        eliminar_producto(productos)
    
    elif opcion == 4:
        actualizar_disponibilidad(productos)

    elif opcion == 5:
        mostrar_inventario(productos)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break