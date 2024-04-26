'''Zadanie 1 (1 punkt + 1 punkt za testy jednostkowe). Napisz własną1 klasę Polynomial, reprezen-
tującą wielomian pojedynczej zmiennej x. Klasa powinna zawierać metody:
 init (self, coefficients) – inicjalizator tworzący wielomian. Parametr coefficients
to lista współczynników wielomianu stojących kolejno przy coraz większych potęgach x.
 deg(self) – zwraca stopień wielomianu.
 str (self) – zwraca napis reprezentujący self.
 neg (self) – zwraca wielomian (instancję Polynomial) odpowiadający −self.
 add (self, other poly) – zwraca wielomian odpowiadający self+other poly.
 sub (self, other poly) – zwraca wielomian odpowiadający self−other poly.
 mul (self, other poly) – zwraca wielomian odpowiadający self·other poly.
 eq (self, other poly) – zwraca True, gdy wielomiany self i other poly są równe i
False w przeciwnym przypadku.
 call (self, x) — zwraca wartość wielomianu w punkcie x.
Następnie (korzystając z modułu unittest) napisz w osobnym pliku testy każdej z metod klasy
Polynomial.'''

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
        suma=0
        for i in range(0, self.deg()+1):
            suma+= self.coef[i] * (x**i)
        return suma

if __name__=="__main__":
    print(del_zeroes([1,0,0,7,0,0,0]) )
    print(del_zeroes([1, 0, 0, 0, 0, 0]))
    print()
    print(add_zeroes([1,2,0], 5) )
    print()
    lst=[1,1,0,-2,3,0]
    x=Polynomial(lst)
    lst.append(33)
    print(x.coef)
    print(lst)
    print(x.deg())
    print(x)
    print(-x)
    y=Polynomial([0,0,1000])
    print(f"({x}) + ({y}) = {x+y}")
    print((x+y).coef)
    print()
    print()
    z=Polynomial([0,20])
    print(f"({y}) - ({z}) = {y-z}")
    z1=Polynomial([0,-20])
    print(-z == z1)

    print()
    print('**********************')
    print( z1(1) , x(0) )

    '''a=Polynomial([1])
    b=Polynomial([0,1])
    print(b)
    print(":*")
    print(f"({a}) * ({b}) = {a *b }")
    print(f"({z1}) * ({b}) = {z1 * b}")

    print((f"({b}) * ({x}) = {b*x}"))

    a = Polynomial([0, 1, -2, 3, 4, 5])
    b = Polynomial([0, 1, -2, 3, 4, 5])
    print(a==b)
    a = Polynomial([])'''