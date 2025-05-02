# Parámetros
TIEMPO_TOTAL = 180  # en minutos
TIEMPO_MAX_JUGADOR = 30
TIEMPO_SESION = 10
AREAS = ["tiros", "defensa", "condicion", "dribling"]

# Pedir datos de jugadores
num_jugadores = int(input("¿Cuántos jugadores hay? "))
jugadores = []

for i in range(num_jugadores):
    print(f"\nIngrese las habilidades para el jugador {i + 1}:")
    nombre = input("Nombre del jugador: ")
    habilidades = {}
    for area in AREAS:
        while True:
            try:
                nivel = int(input(f"Nivel en {area} (1 a 5): "))
                if 1 <= nivel <= 5:
                    habilidades[area] = nivel
                    break
                else:
                    print("Debe estar entre 1 y 5.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
    jugadores.append({"nombre": nombre, "habilidades": habilidades})

# Planificación
plan = []
tiempo_total_utilizado = 0

print("\nAsignando entrenamientos...\n")

for jugador in jugadores:
    nombre = jugador["nombre"]
    habilidades = jugador["habilidades"]
    tiempo_jugador = 0

    # Punto débil
    area_debil = min(habilidades, key=habilidades.get)
    if habilidades[area_debil] < 5:
        habilidades[area_debil] += 1
    tiempo_jugador += TIEMPO_SESION
    tiempo_total_utilizado += TIEMPO_SESION
    plan.append((nombre, area_debil, TIEMPO_SESION))
    print(f"{nombre} entrena en su punto débil: {area_debil} (+1)")

    # Refuerzos
    otras_areas = sorted(habilidades, key=habilidades.get)
    for area in otras_areas:
        if area != area_debil and tiempo_jugador + TIEMPO_SESION <= TIEMPO_MAX_JUGADOR and tiempo_total_utilizado + TIEMPO_SESION <= TIEMPO_TOTAL:
            if habilidades[area] < 5:
                habilidades[area] += 1
            tiempo_jugador += TIEMPO_SESION
            tiempo_total_utilizado += TIEMPO_SESION
            plan.append((nombre, area, TIEMPO_SESION))
            print(f"{nombre} refuerza: {area} (+1)")

# Resultados
print("\n--- PLAN DE ENTRENAMIENTO ---")
for sesion in plan:
    print(f"{sesion[0]} entrenó {sesion[1]} durante {sesion[2]} minutos")

print(f"\nTiempo total utilizado: {tiempo_total_utilizado} minutos")

print("\n--- HABILIDADES FINALES ---")
for jugador in jugadores:
    print(f"{jugador['nombre']}: {jugador['habilidades']}")
