import csv
from product import Product

def save_inventory(products, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([product.codigo, product.nombre, product.marca, product.precio, product.existencias, product.proveedor['codigo'], product.proveedor['nombre'], product.proveedor['pais']])

def load_inventory(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            proveedor = {"codigo": row[5], "nombre": row[6], "pais": row[7]}
            product = Product(row[0], row[1], row[2], float(row[3]), int(row[4]), proveedor)
            products.append(product)
    return products
