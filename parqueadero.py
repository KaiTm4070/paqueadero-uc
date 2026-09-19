CUPOS = 30

#  Datos iniciales 
n = int(input("Cantidad de vehiculos a simular (N): "))

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

    print("Leido:", placa, tipo, hora, horas)
