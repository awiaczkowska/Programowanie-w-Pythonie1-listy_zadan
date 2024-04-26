import sympy as s


def trapezy(x, f, a, b, n):
    suma_pol = 0
    deltaX = s.sympify((b - a) / n)
    # print(deltaX)
    for i in range(0, n):
        x0 = s.sympify(a + i * deltaX)
        x1 = x0 + deltaX
        trapez = s.sympify(deltaX * s.sympify(0.5) * (f.subs(x, x0) + f.subs(x, x1)))
        # print(trapez)
        # print(f.subs(x,x0))
        # rint()
        suma_pol += trapez
    return suma_pol


if __name__ == "__main__":
    x = s.Symbol('x')

    print(trapezy(x, x, 0, 1, 1))
    f = s.sympify(2)
    print(trapezy(x, f, 0, 1, 2))
    print()
    print(trapezy(x, x ** 2, 0, 1, 5))
    print(trapezy(x, x ** 2, 0, 1, 20))
    print(trapezy(x, x ** 2, 0, 1, 100))
    print(trapezy(x, x ** 2, 0, 1, 9999))