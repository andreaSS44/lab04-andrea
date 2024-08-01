
class Product:
    def __init__(self, codigo, nombre, marca, precio, existencias, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.existencias = existencias
        self.proveedor = proveedor

    def __str__(self):
        return f"{self.codigo}, {self.nombre}, {self.marca}, {self.precio}, {self.existencias}, {self.proveedor['nombre']}"
