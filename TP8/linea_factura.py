class LineaFactura:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        
        self.precio_base_historico = producto.precio_base
        self.iva_porcentaje_historico = producto.porcentaje_iva
    
    def calcular_subtotal(self):
        return self.cantidad * self.precio_base_historico
    
    def calcular_iva(self):
        return self.calcular_subtotal() * self.iva_porcentaje_historico

    def calcular_total_linea(self):
        return self.calcular_subtotal() + self.calcular_iva()