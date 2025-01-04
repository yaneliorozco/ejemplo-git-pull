def multiplicar_por_cinco(lista_numeros):
    resultado = [numero * 5 for numero in lista_numeros]
    return resultado

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = multiplicar_por_cinco(numeros)
print(resultado)  # Salida: [5, 10, 15, 20, 25]