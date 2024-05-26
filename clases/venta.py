from datetime import datetime


class Venta:
    def __init__(self,cliente, lista_de_productos):
        self.cliente = cliente
        self.lista_de_productos = lista_de_productos
        self.fecha = datetime.now()
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_de_productos)
    
    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f"Venta registrada: {self.mostrar_informacion()}"
    
    def mostrar_informacion(self):
        productos = ", ".join([producto.nombre for producto in self.lista_de_productos])
        return f"Cliente: {self.cliente.nombre}, Productos: {productos}, Total: {self.total}"