def ShowMenu():
    print (f"""Welcome to you Inventory Simple Manager:
    1. Register a product and its available quantity
    2. Show all products with their quantities.
    3. Search for a product by name.
    4. Change the available quantity of a product.
    5. Remove a product from inventory.
    6. Show how many different products are registered.
    7. Display the product with the largest or smallest available quantity.
    0. Exit menu
    """)
    SelectOption()

def SelectOption():
    option = int(input("Select an option: "))
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
        print("Finalizing program.")
    else: 
        print("Invalid data. Please try again.")
        ShowMenu()

def returnMenu():
    returnMenu = input("Press [Enter] to return to the main menu").lower()
    ShowMenu()

def Option1():
    global products, quantities
    while True:
        name = input("Enter the product name:")
        quatity = int(input("Enter the quantity of the product:"))
        products.append(name)
        quantities.append(quatity)

        print("Product added successfully")

        registerAgain = input("Would you like to register another product? Y/N ").lower()

        if not "y" in registerAgain:
            returnMenu()
            break

def option2():
    if len(products) == 0:
        print("Empty inventory")
    else:
        print("Your inventory")
        for i in range(len(products)):
            print(f"{i + 1}. product: {products[i]} \n quantity: {quantities[i]}")
    returnMenu()

def option3():
    while True:
        name = input("Enter the name of the product you want to search for:")
        if name in products:
            position = products.index(name)
            print("The product was found", name, "in the position", position + 1, "there are", quantities[position], "Items in your inventory.")
        else: print("The product does not exist.")

        SearchAgain = input("Would you like to search for another product? Y/N ").lower()

        if not "y" in SearchAgain:
            returnMenu()
            break

def option4():
    while True:
        name = input("Enter the product name:")

        if name in products:
            position = products.index(name)
            confirmation = input(f"You selected the product: {name} Currently, there are {quantities[position]} Units: Do you want to change the quantity of this product? Y/N ")
            if "y" in confirmation:
                newQuantity = int(input("Enter the new amount:"))
                quantities[position] = newQuantity
                print("the amount of", name, "has been successfully changed to", quantities[position])
            else: returnMenu()
        else: print("The product does not exist.")

        modifyAgain = input("Would you like to change the quantity of another product? Y/N ").lower()

        if not "y" in modifyAgain:
            returnMenu()
            break
def option5():
    while True:
        name = input("Enter the name of the product to be deleted:")
        if name in products:
            position = products.index(name)
            confirmation = input(f"You selected the product: {name} Would you like to remove this product? Y/N ")
            if "y" in confirmation:
                productEliminated = products.pop(position)
                quantities.pop(position)
                print(productEliminated, "has been successfully removed.")
            else: returnMenu()
        else: print("The product does not exist.")

        deleteAgain = input("Would you like to remove another product? Y/N ").lower()
        
        if not "y" in deleteAgain:
            returnMenu()
            break
def option6():
    print(f"Registered products {len(products)}")
    returnMenu()

def option7():
    maximum = quantities.index(max(quantities))
    minimum = quantities.index(min(quantities))
    print(f"The product you have the most of is {products[maximum]} with {quantities[maximum]} items.")
    print(f"The product you have the less of is {products[minimum]} with {quantities[minimum]} items.")
    returnMenu()


products = []
quantities = []

ShowMenu()


