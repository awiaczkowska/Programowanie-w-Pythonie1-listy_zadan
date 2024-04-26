import sympy as s

def del_zeroes(lst):
    "czyscimy z konca listy nieznaczace zera"
    lst.reverse()
    while(lst[0]==0 ):
        if len(lst)==1: return lst
        lst.remove(0)
    lst.reverse()
    return lst
def add_zeroes(lst, LEN):
    "dodajemy zera do uzyskania podanej dlugosci (lub zostawiamy jak jest gdy lista na wejsciu jest dluzsza"
    while (len(lst) < LEN ):
        lst.append(0)
    return lst


class Polynomial:

    def __init__(self, coefficients):
        if len(coefficients) == 0: self.coef=[0]
        else:  self.coef=del_zeroes( coefficients.copy())


    def deg(self):
        return len(self.coef)-1

    def __str__(self):
        Str= str( self.coef[0] )
        for i in range (1, self.deg() +1 ):
            if self.coef[i] < 0 : Str+=f" - { -self.coef[i] } x^{i}"
            else: Str+= f" + { self.coef[i] } x^{i}"
        return Str

    def __neg__(self):
        lst=[]
        for i in range(0,self.deg() +1):
            lst.append( -self.coef[i] )
        return Polynomial(lst)

    def __add__ (self, other_poly):
        lst=[]
        for i in range (0, max(self.deg(), other_poly.deg() ) +1 ):
            if i> self.deg(): lst.append(other_poly.coef[i] )
            elif i > other_poly.deg(): lst.append(self.coef[i])
            else : lst.append(self.coef[i] + other_poly.coef[i] )
        return Polynomial(lst)

    def __sub__ (self, other_poly):
        return(self + (-other_poly) )

    def __mul__ (self, other_poly) :
        wynik=[]
        LEN=(self.deg()+ other_poly.deg() ) +1 # max dlugosc = nr ost elementu +1
        Slst=add_zeroes(self.coef.copy() , LEN)
        Olst=add_zeroes(other_poly.coef.copy(), LEN)
        for n in range (0, LEN):
            suma=0
            for k in range (0, n+1):
                suma+=Slst[k] * Olst[n-k]
            wynik.append(suma)
        return Polynomial(wynik)


    def __eq__(self, other_poly):
        return(self.coef == other_poly.coef)


    def __call__ (self, x):
        '''suma=0
        for i in range(0, self.deg()+1):
            suma+= self.coef[i] * (x**i)
        return suma'''
        t=s.Symbol('t')
        F=s.sympify(0)
        for i in range(0, self.deg() + 1):
            F+=self.coef[i] * t**i

        #s.pprint(F)
        return F.subs(t,x)


if __name__ == "__main__":
    lst = [1, 1, 0, -2, 3, 0]
    W = Polynomial(lst)
s.pprint( W(0) )
s.pprint( W(1) )
s.pprint( W(-1) )