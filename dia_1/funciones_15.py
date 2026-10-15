def get_datos_factura():
	while True:
		nombre_cliente = input("Ingresa el nombre del cliente: ").strip()
		if nombre_cliente:
			break
		print("El nombre del cliente no puede estar vacío.")

	while True:
		producto = input("Ingresa el nombre del producto: ").strip()
		if producto:
			break
		print("El nombre del producto no puede estar vacío.")

	while True:
		try:
			precio = float(input("Ingresa el precio del producto: ").replace(",", "."))
			if precio > 0:
				break
			print("El precio debe ser mayor que 0.")
		except ValueError:
			print("Ingresa un precio válido.")

	while True:
		try:
			cantidad = int(input("Ingresa la cantidad: "))
			if cantidad > 0:
				break
			print("La cantidad debe ser mayor que 0.")
		except ValueError:
			print("Ingresa una cantidad válida.")

	return nombre_cliente, producto, precio, cantidad


def formato_moneda(valor):
	valor_formateado = f"{valor:,.2f}"
	valor_formateado = valor_formateado.replace(",", "_")
	valor_formateado = valor_formateado.replace(".", ",")
	return "$" + valor_formateado.replace("_", ".")