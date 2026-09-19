CUPOS = 30

#  Datos iniciales 
n = int(input("Cantidad de vehiculos a simular (N): "))

# Acumuladores
registrados = 0
total_recaudado = 0.0   
cant_estudiantes = 0
cant_docentes = 0   
cant_visitantes = 0
suma_horas = 0.0

#  Ciclo principal 
procesados = 0
while procesados < n:
    procesados += 1
    print("\n--- Vehiculo", procesados, "de", n, "---")

    # Entrada de datos 
    placa = input("Placa: ")
    tipo = input("Tipo de usuario (E/D/V): ").strip().upper()
    hora = int(input("Hora de entrada (0-23): "))
    horas = float(input("Horas de permanencia: "))

    # Validaciones
    hora_invalida = hora < 0 or hora > 23
    permanencia_invalida = horas <= 0

    if hora_invalida or permanencia_invalida:
        if hora_invalida:
            print("ERROR: la hora de entrada debe estar entre 0 y 23.")
        if permanencia_invalida:
            print("ERROR: las horas de permanencia deben ser mayores que 0.")
        print("Registro rechazado, no se cuenta el vehiculo.")
        continue

    if tipo != "E" and tipo != "D" and tipo != "V":
        print("ADVERTENCIA: tipo de usuario desconocido, se trata como visitante.")
        tipo = "V"

    # Calculo de tarifa
    if tipo == "E":
        if horas <= 2:
            cobro = 0
        else:
            cobro = (horas - 2) * 800
        cant_estudiantes += 1
    elif tipo == "D":
        cobro = horas * 500
        cant_docentes += 1
    else:
        if horas <= 1:
            cobro = 1500
        else:
            cobro = 1500 + (horas - 1) * 1200
        cant_visitantes += 1

    cobro = round(cobro, 2)
    print("Placa", placa, "| Cobro: $" + str(cobro))

    # Acumular estadisticas
    registrados += 1
    total_recaudado += cobro
    suma_horas += horas
