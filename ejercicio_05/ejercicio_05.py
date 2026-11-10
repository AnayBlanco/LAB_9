"""
Ejercicio 5. Extraer valores de una estructura anidada
"""

def extraer_valores(datos):
    resultado = []
    for elemento in datos:
        if isinstance(elemento, list):
            resultado.extend(extraer_valores(elemento))
        else:
            resultado.append(elemento)
    return resultado


# ---------------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------------
# 1. ¿Qué devuelve la función cuando recibe una lista vacía?
# Devuelve una nueva lista vacía [], ya que el ciclo for no realiza ninguna iteración.

# 2. ¿Qué diferencia hay entre incorporar un número e incorporar el resultado de una llamada recursiva?
# Un número se añade individualmente con append(), mientras que el resultado de una llamada recursiva es una lista cuyos elementos se agregan con extend().

# 3. Dibuja únicamente las llamadas a extraer_valores() para [1, [2, [], [3]], 4]. ¿Cuántas llamadas se realizan, incluyendo las de listas vacías?
# Se realizan 5 llamadas en total:
# 1. extraer_valores([1, [2, [], [3]], 4])
# 2. extraer_valores([2, [], [3]])
# 3. extraer_valores([])
# 4. extraer_valores([3])
# 5. Total de llamadas realizadas: 5.

# 4. ¿Por qué cada llamada necesita su propia lista de resultados?
# Porque cada llamada resuelve el aplanamiento de su nivel actual. Devolver su propia lista permite a la llamada superior combinarla con extend() sin alterar otros niveles.


if __name__ == "__main__":
    print(extraer_valores([10, [20, 30], 40]))       # [10, 20, 30, 40]
    print(extraer_valores([1, [2, [], [3]], 4]))     # [1, 2, 3, 4]
    print(extraer_valores([[], [], [[]]]))           # []
    print(extraer_valores([]))                        # []