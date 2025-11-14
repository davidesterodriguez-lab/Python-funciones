def potencia(base, exponente):
    r = 1
    for _ in range(exponente):
        r *= base
    return r
