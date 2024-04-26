'''Zadanie 2 (1,5 punktu). Napisz własną klasę Fraction służącą do reprezentującji ułamków. Zaimplementuj
następujące metody specjalne1:
 init (self, numer=0, denom=1) – inicjalizator tworzący ułamek numer/denom.
 abs (self) – zwraca ułamek odpowiadający |self|.
 neg (self) – zwraca ułamek odpowiadający −self.
 str (self) – zwraca napis reprezentujący self.
 add (self, other frac) – zwraca ułamek odpowiadający self + other frac.
 sub (self, other frac) – zwraca ułamek odpowiadający self − other frac.
 mul (self, other frac) – zwraca ułamek odpowiadający self · other frac.
 truediv (self, other frac) – zwraca ułamek odpowiadający self / other frac.
 eq (self, other frac) – sprawdza, czy self = other frac.
 lt (self, other frac) – sprawdza, czy self < other frac.
Zarówno licznik jak i mianownik ułamka powinny być przechowywane w postaci reprezentującej nieskra-
calny ułamek. Znak ułamka powinien być przechowywany w liczniku2. Do testów możesz użyć analogicznej
klasy Fraction z modułu fractions.'''
from math import gcd
class Fraction:
    def __init__(self, numer=0, denom=1):
        if denom==0: raise ZeroDivisionError("Zero nie moze byc w mianowniku!")
        g=gcd(numer,denom)
        numer=numer/g
        denom=denom/g
        if denom<0 :
            numer*=(-1)
            denom*=(-1)
        self.numer=int(numer)
        self.denom=int(denom)

    def __abs__ (self):
        return Fraction( abs(self.numer), abs(self.denom) )

    def __neg__ (self):
        return Fraction (- self.numer , self.denom )

    def __str__(self):
        return "({}/{})".format(self.numer,self.denom)
        #return f"{self.numer} / {self.denom}" #alternatywny ap

    def __add__ (self, other_frac):
        a = self.numer ; c = other_frac.numer
        b = self.denom ; d = other_frac.denom
        denom=b*d
        numer=a*d + b*c
        return Fraction(numer,denom)
    def __sub__ (self, other_frac):
        return self + (-other_frac)

    def __mul__(self, other_frac):
        return Fraction(self.numer * other_frac.numer , self.denom * other_frac.denom)

    def __truediv__ (self, other_frac):
        odwr = Fraction(other_frac.denom , other_frac.numer )
        return self * odwr

    def __eq__ (self, other_frac):
        return self.numer==other_frac.numer and self.denom==other_frac.denom

    def __lt__ (self, other_frac):
        return self.numer/self.denom < other_frac.numer/other_frac.denom

if __name__=="__main__":
    a=Fraction(1,2)
    b=Fraction(1,4)
    c=Fraction(2,-1)
    d=Fraction(1,2)
    print(d==a)
    print(b<a)
    print(d<a)
    print(a,"+",b,"=",a+b)
    print(a, "-", b, "=", a - b)
    print(a, "/", c, "=", a /c )