"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    pass 

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

codigos = [101, 205, 310, 415, 520, 630, 740]

buscar_codigo(codigos, 520, 0, len(codigos) - 1)  # 4
buscar_codigo(codigos, 300, 0, len(codigos) - 1)  # -1
buscar_codigo([], 300, 0, -1)                      # -1
buscar_codigo([205], 205, 0, 0)                   # 0

Restricciones

- La solución debe ser recursiva.
- No me utilices ciclos ni cortes.
- No busques con objetivo en codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""

def buscar_codigo(codigos, objetivo, izquierda, derecha):
    # Caso base 1: El rango de búsqueda es inválido (elemento no encontrado)
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    # Caso base 2: Elemento encontrado en la posición media
    if codigos[medio] == objetivo:
        return medio
    
    # Paso recursivo: buscar a la izquierda si el objetivo es menor
    if objetivo < codigos[medio]:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)
    # Paso recursivo: buscar a la derecha si el objetivo es mayor
    else:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)


# ---------------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
# Termina cuando se encuentra el elemento (codigos[medio] == objetivo) o cuando el índice izquierda supera al índice derecha (izquierda > derecha), lo que indica que el elemento no está presente.

# 2. ¿Por qué no debes incluir nuevamente la posición central en el siguiente intervalo?
# Porque el elemento en la posición central ya fue evaluado y se confirmó que no es igual al objetivo.

# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a calcular el medio, escribe "-".
# Llamada | Izquierda | Derecha | Medio | Decisión
# --------------------------------------------------
#    1    |     0     |    6    |   3   | Ir a la izquierda (300 < 415)
#    2    |     0     |    2    |   1   | Ir a la derecha (300 > 205)
#    3    |     2     |    2    |   2   | Ir a la izquierda (300 < 310)
#    4    |     2     |    1    |   -   | Caso base: no encontrado (-1)

# 4. ¿Qué diferencia hay entre el progreso de esta función y el de contar_desde_limite()?
# contar_desde_limite() avanza de uno en uno descartando un solo elemento por llamada (O(N)), mientras que buscar_codigo() divide el espacio de búsqueda a la mitad en cada paso descartando la mitad de los elementos (O(log N)).

if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))  # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))  # -1
    print(buscar_codigo([], 300, 0, -1))                     # -1
    
