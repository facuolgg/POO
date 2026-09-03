class ImpresorFactura:
    """
    Fabricación Pura: no representa ningún concepto del dominio del negocio
    (no es ni una Factura, ni un Producto, ni una LineaFactura).
    Su única responsabilidad es la PRESENTACIÓN. No calcula nada: solo
    lee valores ya resueltos por Factura y les da formato en pantalla.
    """

    @staticmethod
    def imprimir(factura):
        totales = factura.calcular_totales()

        print("=" * 60)
        print(f"  FACTURA TIPO {factura.tipo_comprobante}")
        print("=" * 60)
        print("\n  DETALLE DE PRODUCTOS:")
        print("-" * 60)

        for i, linea in enumerate(totales["detalle_lineas"], 1):
            print(f"  {i}. {linea['nombre_producto']}")
            print(f"     Cantidad: {linea['cantidad']}")
            print(f"     Precio base: ${linea['precio_base']:.2f}")

            if linea["porcentaje_descuento"] > 0:
                print(f"     Descuento: {linea['porcentaje_descuento']*100:.0f}%")
                print(f"     Precio con descuento: ${linea['precio_con_descuento']:.2f}")

            print(f"     Subtotal: ${linea['subtotal']:.2f}")
            print(f"     IVA ({linea['iva_porcentaje']*100:.1f}%): ${linea['iva']:.2f}")
            print(f"     Total línea: ${linea['total_linea']:.2f}")
            print()

        print("-" * 60)
        print("  RESUMEN DE TOTALES:")
        print("-" * 60)
        print(f"  Total Neto: ${totales['total_neto']:.2f}")

        print(f"\n  DESGLOSE DE IVA:")
        if totales['total_iva_21'] > 0:
            print(f"    IVA 21%: ${totales['total_iva_21']:.2f}")
        if totales['total_iva_105'] > 0:
            print(f"    IVA 10.5%: ${totales['total_iva_105']:.2f}")
        if totales['total_iva_otros'] > 0:
            print(f"    IVA otros: ${totales['total_iva_otros']:.2f}")

        print(f"\n  Total IVA: ${totales['total_iva']:.2f}")
        print("-" * 60)
        print(f"  TOTAL A PAGAR: ${totales['total_final']:.2f}")
        print("=" * 60)
