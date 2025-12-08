def operaciones_conjuntos(lista1: list[int], lista2: list[int]) -> dict:

    # se convierten las listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    #intersección
    interseccion = conjunto1.intersection(conjunto2)

    #unión
    union = conjunto1.union(conjunto2)

    #diferencia simétrica
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

    return {
        "interseccion": sorted(list(interseccion)),
        "union": sorted(list(union)),
        "diferencia_simetrica": sorted(list(diferencia_simetrica)),
    }

#programa de prueba

l1 = [11, 22, 13, 4, 5, 6]
l2 = [4, 15, 6, 7, 81, 9]

resultados = operaciones_conjuntos(l1, l2)

print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")
print("\nResultados de las operaciones con conjuntos:")
for operacion, resultado in resultados.items():
    print(f"- {operacion.capitalize()}: {resultado}")
