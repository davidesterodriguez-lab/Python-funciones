def contar_digitos(n):
    n = abs(n)
    c = 0
    if n == 0:
        return 1
    while n > 0:
        n //= 10
        c += 1
    return c

resultado = int(input("Ingrese un numero: "))
print (contar_digitos(resultado))
