def procesar_lista(lista_numeros: list[int]) -> list[int]:

  return sorted(set(num for num in lista_numeros if num >= 0)) 
# se itera sobre la lista y se cogen los número mayores de cero para eliminar los negativos
# con set se dejan solo los elementos únicos y sorted la ordena de menor a mayor

lista_ejemplo = [4, -1, 7, 4, -3, 5, 2, -5, 2]
resultado = procesar_lista(lista_ejemplo)

print(f"Lista original: {lista_ejemplo}")
print(f"Lista procesada: {resultado}")
