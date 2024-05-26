class Inventario:
    def __init__(self):
        self.lista_de_productos = []

    def agregar_producto(self, producto):
        self.lista_de_productos.append(producto)

    def actualizar_inventario(self, producto, cantidad):
        for prod in self.lista_de_productos:
            if prod.nombre == producto.nombre:
                prod.actualizar_cantidad(cantidad)
    
    def generar_alerta(self, umbral_minimo):
        alertas = [prod.nombre for prod in self.lista_de_productos if prod.cantidad < umbral_minimo]
        return f"Productos por debajo del umbral: {', '.join(alertas)}" if alertas else "No hay ningún producto por debajo del umbral minimo determinado"