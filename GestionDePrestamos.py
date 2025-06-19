# Aplicación de Gestión de Préstamos

prestamos = []

def solicitar_monto():
    while True:
        try:
            monto = float(input("Ingrese el monto del préstamo: "))
            if monto <= 0:
                print("El monto debe ser mayor que cero.")
            else:
                return monto
        except ValueError:
            print("Solo se permiten números.")

def registrar_prestamo():
    nombre = input("Ingrese el nombre del prestatario: ").strip().title()
    monto = solicitar_monto()
    fecha = input("Ingrese la fecha del préstamo (como : 2025-06-15): ").strip()
    prestamo = {
        "nombre": nombre,
        "monto": monto,
        "fecha": fecha,
        "estado": "pendiente"
    }
    prestamos.append(prestamo)
    print("Préstamo registrado con éxito. Buena decisión")

def ver_historial():
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        print("Historial de Préstamos:")
        for i, p in enumerate(prestamos, start=1):
            print(f"{i}. Nombre: {p['nombre']} | Monto: ${p['monto']} | Fecha: {p['fecha']} | Estado: {p['estado']}")
    print()

def buscar_por_nombre():
    nombre = input("nombre del prestatario a buscar: ").strip().title()
    encontrados = [p for p in prestamos if p["nombre"] == nombre]
    if encontrados:
        print(f"Préstamos encontrados para {nombre}:")
        for i, p in enumerate(encontrados, start=1):
            print(f"{i}. Monto: ${p['monto']} | Fecha: {p['fecha']} | Estado: {p['estado']}")
    else:
        print("No encontramos préstamos para ese nombre.")
    print()

def marcar_como_pagado():
    nombre = input("Ingrese el nombre del prestatario a marcar como pagado: ").strip().title()
    encontrados = [p for p in prestamos if p["nombre"] == nombre and p["estado"] == "pendiente"]
    if not encontrados:
        print("No hay préstamos pendientes para ese nombre.")
        return

    print("Préstamos pendientes:")
    for i, p in enumerate(encontrados, start=1):
        print(f"{i}. Monto: ${p['monto']} | Fecha: {p['fecha']}")

    try:
        eleccion = int(input("Seleccione el número del préstamo a marcar como pagado: "))
        if 1 <= eleccion <= len(encontrados):
            index_real = prestamos.index(encontrados[eleccion - 1])
            prestamos[index_real]["estado"] = "pagado"
            print("Préstamo marcado como pagado.")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")


# Muestra el total prestado y cuánto falta por pagar
def mostrar_totales():
    total = sum(p["monto"] for p in prestamos)
    pendiente = sum(p["monto"] for p in prestamos if p["estado"] == "pendiente")
    print(f"Total prestado: ${total:.2f}")
    print(f"Total pendiente por pagar: ${pendiente:.2f}")
    print()


#menu de inicio
def menu():
    while True:
        print("===== Menú Principal - Gestión de Préstamos =====")
        print("1. Registrar un nuevo préstamo")
        print("2. Ver historial de préstamos")
        print("3. Buscar préstamos por nombre")
        print("4. Marcar préstamo como pagado")
        print("5. Mostrar totales")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            buscar_por_nombre()
        elif opcion == "4":
            marcar_como_pagado()
        elif opcion == "5":
            mostrar_totales()
        elif opcion == "6":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
