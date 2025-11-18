def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

num = int(input("Ingrese un numero: "))
print (("Su factorial es :" ), factorial(num))