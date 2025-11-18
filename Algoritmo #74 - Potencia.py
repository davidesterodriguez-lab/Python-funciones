def potencia(base, exponente):
    r = 1
    for i in range(exponente):
        r *= base
    return r
base= float(input("Ingrese un numero: "))
exponente = int(input("Ingrese una potencia: "))
print (potencia (base, exponente))