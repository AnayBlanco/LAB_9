"""
Ejercicio 6 (reto). Reporte de ventas por sucursal

Una empresa guarda las ventas de cada sucursal en un diccionario. Los valores
pueden estar agrupados en listas anidadas.
"""

# Reutilización del ejercicio 5 para extraer valores planos
def extraer_valores(datos):
    resultado = []
    for elemento in datos:
        if isinstance(elemento, list):
            resultado.extend(extraer_valores(elemento))
        else:
            resultado.append(elemento)
    return resultado


# Parte A. Suma con acumulador (Recursiva de cola)
def sumar_cola(valores, i=0, acumulado=0):
    """Suma desde la posición i hasta el final, agregada a acumulado."""
    if i >= len(valores):
        return acumulado
    return sumar_cola(valores, i + 1, acumulado + valores[i])


# Parte B. Reporte integrado
def reporte_sucursales(ventas):
    lista_sucursales = []
    total_general = 0
    
    for nombre, registros in ventas.items():
        valores_planos = extraer_valores(registros)
        cantidad_ventas = len(valores_planos)
        total_sucursal = sumar_cola(valores_planos)
        
        total_general += total_sucursal
        
        lista_sucursales.append({
            "nombre": nombre,
            "cantidad_ventas": cantidad_ventas,
            "total": total_sucursal
        })
        
    return {
        "sucursales": lista_sucursales,
        "total_general": total_general
    }


# ---------------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------------
# 1. ¿Qué devuelve ventas.items() en cada iteración?
# Devuelve una tupla que contiene la clave (nombre de la sucursal) y el valor asociado (la lista de registros de ventas de dicha sucursal).

# 2. ¿Qué responsabilidad tiene cada una de estas funciones?
# - extraer_valores(): Se encarga de aplanar cualquier estructura de listas anidadas para obtener una lista única con todos los números individuales de ventas.
# - sumar_cola(): Se encarga de calcular la suma de los elementos de una lista plana de forma recursiva usando un acumulador en posición de cola.
# - reporte_sucursales(): Se encarga de iterar sobre el diccionario de ventas, coordinar las funciones anteriores para construir los datos de cada sucursal y consolidar el reporte final con el total general.

# 3. Completa la traza de sumar_cola([10, 20, 30]):
# Llamada | i | acumulado
# ------------------------
#    1    | 0 |     0
#    2    | 1 |    10
#    3    | 2 |    30
#    4    | 3 |    60

# 4. ¿Por qué sumar_cola() es recursiva de cola?
# Porque la llamada recursiva es la última operación que realiza la función. No queda ninguna operación pendiente (como una suma) después de recibir el retorno de la siguiente llamada.

# 5. ¿En cuál de estas dos expresiones queda una suma pendiente después de la llamada?
# Queda una suma pendiente en la expresión `return valores[i] + sumar(valores, i + 1)`, ya que la adición del elemento actual debe esperar a que finalice y retorne la llamada recursiva.


if __name__ == "__main__":
    print(sumar_cola([10, 20, 30]))        # 60
    print(sumar_cola([]))                  # 0
    print(sumar_cola([10, 20, 30], 1))     # 50
    print(sumar_cola([10, 20], 0, 100))    # 130

    ventas = {
        "Centro": [120, [80, 50]],
        "Norte": [],
        "Sur": [[200], [100, [25]]]
    }

    print(reporte_sucursales(ventas))
    print(reporte_sucursales({}))