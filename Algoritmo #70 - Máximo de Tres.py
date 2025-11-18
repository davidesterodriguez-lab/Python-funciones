def maximo_de_tres(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m

num = (int(input("Ingrese el numero 1: ")))
num2 = (int(input("Ingrese el numero 2: ")))
num3 = (int(input("Ingrese el numero 3: ")))

print ("El numero mayor es: ", maximo_de_tres(num, num2, num3))