
from linea_factura import LineaFactura


class Factura:
    def __init__(self, tipo_comprobante, lineas):
        self.tipo_comprobante = tipo_comprobante  # "A" o "B"
        self.lineas = lineas  # Lista de LineaFactura
    
    def calcular_totales(self):
        total_neto = 0.0
        total_iva_21 = 0.0
        total_iva_105 = 0.0
        total_iva_otros = 0.0
        total_iva_general = 0.0

        detalle_lineas = []  # Datos ya resueltos, listos para mostrar

        for linea in self.lineas:
            precio_con_descuento = linea.calcular_precio_con_descuento()
            subtotal = linea.calcular_subtotal()
            iva = linea.calcular_iva()
            total_linea = linea.calcular_total_linea()

            total_neto += subtotal

            if linea.iva_porcentaje_historico == 0.21:
                total_iva_21 += iva
            elif linea.iva_porcentaje_historico == 0.105:
                total_iva_105 += iva
            else:
                total_iva_otros += iva

            total_iva_general += iva

            detalle_lineas.append({
                "nombre_producto": linea.producto.nombre,
                "cantidad": linea.cantidad,
                "precio_base": linea.precio_base_historico,
                "porcentaje_descuento": linea.porcentaje_descuento_linea,
                "precio_con_descuento": precio_con_descuento,
                "subtotal": subtotal,
                "iva_porcentaje": linea.iva_porcentaje_historico,
                "iva": iva,
                "total_linea": total_linea,
            })

        total_final = total_neto + total_iva_general

        return {
            "detalle_lineas": detalle_lineas,
            "total_neto": total_neto,
            "total_iva_21": total_iva_21,
            "total_iva_105": total_iva_105,
            "total_iva_otros": total_iva_otros,
            "total_iva": total_iva_general,
            "total_final": total_final,
        }
