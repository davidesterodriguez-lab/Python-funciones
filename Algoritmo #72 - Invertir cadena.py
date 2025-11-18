def invertir(cadena):
    if len(cadena) <= 1:
        return cadena
    return invertir(cadena[1:]) + cadena[0]

resultado = str(input("Ingrese alguna palabra: "))
print (invertir(resultado))
