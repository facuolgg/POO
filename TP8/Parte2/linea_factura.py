
class LineaFactura:
    def __init__(self, producto, cantidad, porcentaje_descuento_linea=0.0):
        self.producto = producto
        self.cantidad = cantidad
        self.porcentaje_descuento_linea = porcentaje_descuento_linea
        
        self.precio_base_historico = producto.precio_base
        self.iva_porcentaje_historico = producto.porcentaje_iva
    
    def calcular_precio_con_descuento(self):
        precio_base = self.precio_base_historico
        descuento = precio_base * self.porcentaje_descuento_linea
        return precio_base - descuento
    
    def calcular_subtotal(self):
        return self.cantidad * self.calcular_precio_con_descuento()
    
    def calcular_iva(self):
        return self.calcular_subtotal() * self.iva_porcentaje_historico
    
    def calcular_total_linea(self):
        return self.calcular_subtotal() + self.calcular_iva()
    
    def obtener_tipo_iva(self):
        if self.iva_porcentaje_historico == 0.21:
            return "21"
        elif self.iva_porcentaje_historico == 0.105:
            return "10.5"
        else:
            return f"{self.iva_porcentaje_historico*100:.1f}"