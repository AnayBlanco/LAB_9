"""
Ejercicio 3. Reporte de calificaciones por grupo

Una institución guarda las calificaciones de sus grupos en una lista de listas:

    grupos = [
        [80, 55, 90],
        [],
        [40, 60, 75, 59]
    ]

Implementa:

    def reporte_grupos(grupos, nota_minima=60):
        pass

La función debe devolver una lista de diccionarios. Cada diccionario contiene:

- "grupo": número del grupo, comenzando en 1.
- "cantidad": cantidad de estudiantes.
- "aprobados": cantidad de notas mayores o iguales que nota_minima.
- "reprobados": cantidad de notas menores que nota_minima.

Ejemplo

    reporte_grupos([
        [80, 55, 90],
        [],
        [40, 60, 75, 59]
    ])

Resultado esperado:

    [
        {"grupo": 1, "cantidad": 3, "aprobados": 2, "reprobados": 1},
        {"grupo": 2, "cantidad": 0, "aprobados": 0, "reprobados": 0},
        {"grupo": 3, "cantidad": 4, "aprobados": 2, "reprobados": 2}
    ]

Para una lista de grupos vacía:

    reporte_grupos([])   # []

Requisitos

- Utiliza obligatoriamente:

    for numero_grupo, notas in enumerate(grupos, start=1):
        ...

- Reutiliza la función recursiva contar_desde_limite() del ejercicio 2 para
  obtener los aprobados. El archivo ya trae la importación:

    from ejercicio_02.ejercicio_02 import contar_desde_limite

- Calcula los reprobados a partir de la cantidad total y los aprobados.
- No imprimas el reporte: devuélvelo.
- No modifiques las listas recibidas.

Ejecuta este archivo desde la carpeta principal con:
    python -m ejercicio_03.ejercicio_03
"""


def reporte_grupos(grupos, nota_minima=60):
    reporte = []
    
    for numero_grupo, notas in enumerate(grupos, start=1):
        total_estudiantes = len(notas)
        aprobados = contar_desde_limite(notas, nota_minima)
        reprobados = total_estudiantes - aprobados
        
        reporte.append({
            "grupo": numero_grupo,
            "cantidad": total_estudiantes,
            "aprobados": aprobados,
            "reprobados": reprobados
        })
        
    return reporte


# ---------------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------------
# 1. ¿Qué devuelve enumerate() en cada iteración?
# Devuelve una tupla con el contador actual (iniciando en 1 por start=1) y el elemento correspondiente de la lista (las notas del grupo).

# 2. ¿Qué parte del problema resuelve el ciclo?
# Resuelve el recorrido iterativo de cada uno de los grupos contenidos en la lista principal.

# 3. ¿Qué parte resuelve la función recursiva?
# Resuelve el conteo de calificaciones que son mayores o iguales a la nota mínima dentro de cada grupo.

# 4. ¿Por qué un grupo vacío debe aparecer en el reporte aunque no tenga estudiantes?
# Porque representa un grupo registrado formalmente en la institución, indicando que su cantidad de estudiante, aprobados y reprobados es 0.


if __name__ == "__main__":
    grupos = [
        [80, 55, 90],
        [],
        [40, 60, 75, 59]
    ]
    print(reporte_grupos(grupos))
    print(reporte_grupos([]))   # []
