def ShowMenu():
    print (f"""Bienvenido/a al gestor de inventarios:
    1. Registrar un producto y su cantidad disponible
    2. Mostrar todos los productos con su cantidad.
    3. Buscar un producto por su nombre.
    4. Modificar la cantidad disponible de un producto.
    5. Eliminar un producto del inventario.
    6. Mostrar cuántos productos diferentes hay registrados.
    7. Mostrar el producto con la mayor o menor cantidad disponible. 
    0. Salir del menú
    """)
    SelectOption()

def SelectOption():
    option = int(input("Seleccione una opción: "))
    if option == 1:
        Option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        option6()
    elif option == 7:
        option7()
    elif option == 0:
        print("Finalizando programa.")
    else: 
        print("dato invalido, intentelo nuevamente.")
        ShowMenu()

def returnMenu():
    returnMenu = input("Pulsa [enter] para volver al menú principal").lower()
    ShowMenu()

def Option1():
    global products, quantities
    while True:
        name = input("Ingresa el nombre del producto: ")
        quatity = int(input("Ingresa la cantidad de producto: "))
        products.append(name)
        quantities.append(quatity)

        print("Producto agregado correctamente")

        registerAgain = input("¿Deseas registrar otro producto? s/n ").lower()

        if not "s" in registerAgain:
            returnMenu()
            break

def option2():
    if len(products) == 0:
        print("Inventario vacio")
    else:
        print("Tu inventario:")
        for i in range(len(products)):
            print(f"{i + 1}. producto: {products[i]} \n cantidad: {quantities[i]}")
    returnMenu()

def option3():
    while True:
        name = input("Ingresa el nombre del producto a buscar: ")
        if name in products:
            position = products.index(name)
            print("Se encontró el procuto", name, "en la posición", position + 1, "hay", quantities[position], "unidades en tu inventario.")
        else: print("El producto no existe.")

        SearchAgain = input("¿Deseas buscar otro producto? s/n ").lower()

        if not "s" in SearchAgain:
            returnMenu()
            break

def option4():
    while True:
        name = input("Ingresa el nombre del producto: ")

        if name in products:
            position = products.index(name)
            confirmation = input(f"Seleccionaste el producto: {name} Actualmente hay {quantities[position]} Unidades ¿Deseas modificar la cantidad de unidades de este producto? s/n")
            if "s" in confirmation:
                newQuantity = int(input("Ingresa la nueva cantidad: "))
                quantities[position] = newQuantity
                print("la cantidad de", name, "se ha cambiado exitosamente a", quantities[position])
            else: returnMenu()
        else: print("El producto no existe.")

        modifyAgain = input("¿Deseas modificar la cantidad de otro producto? s/n ").lower()

        if not "s" in modifyAgain:
            returnMenu()
            break
def option5():
    while True:
        name = input("Ingrese el nombre del producto a eliminar: ")
        if name in products:
            position = products.index(name)
            confirmation = input(f"Seleccionaste el producto: {name} ¿Deseas eliminar este producto? s/n")
            if "s" in confirmation:
                productEliminated = products.pop(position)
                quantities.pop(position)
                print(productEliminated, "se ha eliminado exitosamente.")
            else: returnMenu()
        else: print("El producto no existe.")

        deleteAgain = input("¿Deseas eliminar otro producto? s/n ").lower()
        
        if not "s" in deleteAgain:
            returnMenu()
            break
def option6():
    print(f"Productos regitrados {len(products)}")
    returnMenu()

def option7():
    maximum = quantities.index(max(quantities))
    minimum = quantities.index(min(quantities))
    print(f"Tu producto con la mayor cantidad disponible es {products[maximum]} con {quantities[maximum]} unidades.")
    print(f"Tu producto con la menor cantidad disponible es {products[minimum]} con {quantities[minimum]} unidades.")


products = []
quantities = []

ShowMenu()


