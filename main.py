from product import Product
import archivos

def add_product(products):
    codigo = input("Enter product code: ")
    nombre = input("Enter product name: ")
    marca = input("Enter brand: ")
    precio = float(input("Enter price: "))
    existencias = int(input("Enter stock: "))
    proveedor = {
        "codigo": input("Enter supplier code: "),
        "nombre": input("Enter supplier name: "),
        "pais": input("Enter supplier country: ")
    }
    product = Product(codigo, nombre, marca, precio, existencias, proveedor)
    products.append(product)

def remove_product(products):
    codigo = input("Enter product code to remove: ")
    products = [product for product in products if product.codigo != codigo]

def update_product_price(products):
    codigo = input("Enter product code to update price: ")
    for product in products:
        if product.codigo == codigo:
            new_price = float(input("Enter new price: "))
            product.precio = new_price
            break

def list_products(products):
    if not products:
        print("No products available.")
        return
    print("Product List:")
    for product in products:
        print(product)

def search_product(products):
    codigo = input("Enter product code to search: ")
    for product in products:
        if product.codigo == codigo:
            print(product)
            break
    else:
        print("Product not found.")

def main_menu():
    products = []
    while True:
        print("\nMenu:")
        print("1. Add product")
        print("2. Remove product")
        print("3. Update product price")
        print("4. List products")
        print("5. Search product")
        print("6. Save inventory to file")
        print("7. Load inventory from file")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_product(products)
        elif choice == "2":
            remove_product(products)
        elif choice == "3":
            update_product_price(products)
        elif choice == "4":
            list_products(products)
        elif choice == "5":
            search_product(products)
        elif choice == "6":
            archivos.save_inventory(products, 'inventario.txt')
        elif choice == "7":
            products = archivos.load_inventory('inventario.txt')
        elif choice == "8":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
