import copy
import matplotlib.pyplot as plt
import numpy as np

# Parámetros
TIEMPO_TOTAL = 180  # en minutos
TIEMPO_MAX_JUGADOR = 30
TIEMPO_SESION = 10
AREAS = ["tiros", "defensa", "condicion", "dribling"]

# Pedir datos de jugadores
while True:
    try:
        num_jugadores = int(input("¿Cuántos jugadores hay? "))
        if num_jugadores > 0:
            break
        else:
            print("Debe haber al menos un jugador.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

jugadores = []

for i in range(num_jugadores):
    print(f"\nIngrese las habilidades para el jugador {i + 1}:")

    while True:
        nombre = input("Nombre del jugador: ").strip()
        if nombre:
            if nombre not in [j["nombre"] for j in jugadores]:
                break
            else:
                print("Ese nombre ya está registrado, usa uno distinto.")
        else:
            print("El nombre no puede estar vacío.")

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

    habilidades_iniciales = copy.deepcopy(habilidades)
    jugadores.append({
        "nombre": nombre,
        "habilidades": habilidades,
        "habilidades_iniciales": habilidades_iniciales,
        "tiempo_usado": 0
    })

# Planificación
plan = []
tiempo_total_utilizado = 0

print("\nAsignando entrenamientos...\n")

while tiempo_total_utilizado + TIEMPO_SESION <= TIEMPO_TOTAL:
    progreso = False
    for jugador in jugadores:
        if jugador["tiempo_usado"] + TIEMPO_SESION > TIEMPO_MAX_JUGADOR:
            continue  # Saltar si ya alcanzó el máximo

        habilidades = jugador["habilidades"]
        nombre = jugador["nombre"]

        # Buscar el área con menor nivel (punto débil primero)
        posibles_areas = sorted(AREAS, key=lambda area: (habilidades[area], area))
        for area in posibles_areas:
            if habilidades[area] < 5:
                habilidades[area] += 1
                jugador["tiempo_usado"] += TIEMPO_SESION
                tiempo_total_utilizado += TIEMPO_SESION
                plan.append((nombre, area, TIEMPO_SESION))
                print(f"{nombre} entrena {area} (+1)")
                progreso = True
                break  # Solo una sesión por iteración por jugador

        if tiempo_total_utilizado + TIEMPO_SESION > TIEMPO_TOTAL:
            break

    if not progreso:
        break  # No hay más mejoras posibles, se rompe para evitar bucle infinito


# Resultados
print("\n--- PLAN DE ENTRENAMIENTO ---")
for sesion in plan:
    print(f"{sesion[0]} entrenó {sesion[1]} durante {sesion[2]} minutos")

print(f"\nTiempo total utilizado: {tiempo_total_utilizado} minutos")

print("\n--- HABILIDADES FINALES ---")
for jugador in jugadores:
    print(f"{jugador['nombre']}: {jugador['habilidades']}")

# Resumen de progreso total
print("\n--- RESUMEN DE ENTRENAMIENTO ---")
for jugador in jugadores:
    nombre = jugador["nombre"]
    print(f"\n{nombre.upper()}:")
    print(f"  Tiempo total de entrenamiento: {jugador['tiempo_usado']} minutos")
    print("  Mejoras por área:")
    for area in AREAS:
        mejora = jugador["habilidades"][area] - jugador["habilidades_iniciales"][area]
        print(f"    {area}: +{mejora}")

# Gráfico de radar
labels = AREAS
num_vars = len(labels)

# Crear ángulos para las áreas
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Colores únicos por jugador
colors = plt.cm.tab10(np.linspace(0, 1, len(jugadores)))

for idx, jugador in enumerate(jugadores):
    nombre = jugador["nombre"]
    inicial = [jugador["habilidades_iniciales"][area] for area in labels]
    final = [jugador["habilidades"][area] for area in labels]

    inicial += inicial[:1]
    final += final[:1]

    color = colors[idx]

    # Línea antes (discontinua)
    ax.plot(angles, inicial, linestyle='dashed', color=color, label=f'{nombre} (Antes)')
    # Línea después (continua)
    ax.plot(angles, final, linestyle='solid', color=color, label=f'{nombre} (Después)')

# Configuración del gráfico
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_ylim(0, 5)
ax.set_title("Progreso de habilidades de jugadores", size=16)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()

