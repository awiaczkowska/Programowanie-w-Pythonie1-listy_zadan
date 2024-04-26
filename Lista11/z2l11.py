import sympy as s


def ciagla(f,x,x0):
    L=s.limit(f, x, x0, dir="-")
    P=s.limit(f, x, x0, dir="+")
    return L.equals(P)

if __name__=="__main__":
    x = s.Symbol('x')
    t = s.Symbol('t')
    p = s.Piecewise((x + 2, x < 5), (-x - 5, x > 5))
    print(ciagla(x**2, x, 2))
    print(ciagla(t ** 8 + 2 * t, t, 0))
    print(ciagla(x ** 4+6, t, 2)) #fkcja stala ze wzgl na t
    print(ciagla(p, x, 5)) #nieciagla
    print(ciagla(p, t, 5)) #fkcja stala ze wzgl na t

    q = s.Piecewise((x + 2, x < 5), (-x - 5, x > 5), (-100, x==5))
    print(ciagla(q, x, 5))#nieciagla

