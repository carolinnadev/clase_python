from funciones_15 import get_datos_factura, formato_moneda


nombre_cliente, producto, precio, cantidad = get_datos_factura()
subtotal = precio * cantidad

if subtotal >= 500000:
	descuento = subtotal * 0.15
elif subtotal >= 200000:
	descuento = subtotal * 0.10
else:
	descuento = 0

total_pagar = subtotal - descuento



print("\n" + "=" * 40)
print("              FACTURA")
print("=" * 40)
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: {formato_moneda(precio)}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {formato_moneda(subtotal)}")
print(f"Descuento: {formato_moneda(descuento)}")
print(f"Total a pagar: {formato_moneda(total_pagar)}")
print("=" * 40)
