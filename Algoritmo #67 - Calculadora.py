def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    op = input("Operación (+, -, *, /): ")
    if op == "+":
        print(sumar(a, b))
    elif op == "-":
        print(restar(a, b))
    elif op == "*":
        print(multiplicar(a, b))
    elif op == "/" and b != 0:
        print(dividir(a, b))
    else:
        print("Opcion invalida")
calculadora()