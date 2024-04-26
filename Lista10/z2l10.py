'''Zadanie 2 (1 punkt + 1 punkt za testy jednostkowe). Napisz klasę Urn reprezentującą urnę za-
wierającą kule różnych kolorów. Kolory kul są reprezentowane przez napisy. Klasa ma zawierać
następujące metody:
 init (self, balls) — parametr balls to lista par postaci (color, n), gdzie color jest
kolorem (napisem), a n liczbą naturalną. Każda para reprezentuje początkową ilość kul w
danym kolorze znajdującą się w urnie. Konstruktor ma rzucić wyjątek, gdy co najmniej jedna
z podanych ilości kul jest ujemna.

 add(self, color, n) — dokłada do urny n kul w kolorze color. Rzuca wyjątek, gdy n <
0. Przed wykonaniem metody, urna nie musi zawierać kul w kolorze color.

 remove(self, color, n) — usuwa z urny n kul w kolorze color. Rzuca wyjątek, gdy w
urnie nie ma tylu kul w tym kolorze.

 get(self, color) — zwraca ilość kul w kolorze color jaka znajduje się w urnie.

 transfer(self, other urn) — przenosi wszystkie kule z urny self do urny other urn.

 draw chance(self, color) — zwraca ułamek typu Fraction2 reprezentujący prawdopodo-
bieństwo, że losowa kula wyciągnięta z urny (przyjmując, że każda kula może być wyciągnięta
z równą szansą) będzie koloru color. Rzuca wyjątek, gdy w urnie nie ma kul.

 str (self) — zwraca napis reprezentujący self.

 eq (self, other urn) — zwraca True, gdy urny self i other urn zawierają te same
ilości kul w tych samych kolorach, False w przeciwnym wypadku.
Następnie (korzystając z modułu unittest) napisz w osobnym pliku testy każdej z metod klasy
Urn'''
from z2l9 import Fraction

class Urn:
    def __init__ (self, balls):
        self.balls={}
        for tup in balls:
            if tup[1]<0 : raise ValueError("Podano ujemna liczbe kul!")
            if tup[1]>0:
                if tup[0] in self.balls: self.add(tup[0], tup[1])
                else: self.balls[ tup[0] ]= tup[1]

    def add(self, color, n):
        if n<0: raise ValueError("Podano ujemna liczbe kul!")
        elif n==0: return None
        elif color in self.balls: self.balls[color]+=n
        else: self.balls[color]=n

    def remove(self, color, n):
        if n < 0: raise ValueError("Podano ujemna liczbe kul!")
        elif color not in self.balls: raise ValueError(f"W urnie nie ma tylu kul koloru {color}!")
        elif self.balls[color]<n: raise ValueError(f"W urnie nie ma tylu kul koloru {color}!")
        else:
            self.balls[color]-=n
            if self.balls[color]==0: del(self.balls[color])

    def get(self, color):
        if color in self.balls: return self.balls[color]
        else: return 0

    def transfer(self, other_urn):
        if id(other_urn)==id(self): raise ValueError("Podano ta sama urne jako oba parametry!")

        colors=[]
        for col in self.balls:
            other_urn.add(col, self.balls[col])
            colors.append(col)
        for col in colors: del(self.balls[col])

    def draw_chance(self, color):
        if len(self.balls)==0 : raise ZeroDivisionError("Urna jest pusta!")
        if color not in self.balls: return Fraction(0)
        suma=0
        for col in self.balls:
            suma+=self.balls[col]
        return Fraction(self.balls[color],suma)

    def __str__ (self):
        return str(self.balls)

    def __eq__(self,other_urn):
        return self.balls==other_urn.balls


if __name__ == "__main__":
    '''    a=Urn( [("blue",3)] )
    print(a.balls)
    a.add("blue", 3)
    b=Urn( [("blue",6)] )
    c=Urn( [ ("blue",3),("red", 3) ])
    print(a==b)
    print(a.add("red", 3)== c)'''

    print()
    d = Urn([("blue", 1), ("red", 3), ("blue", 2)])
    print(d.balls)

    print()
    b = Urn([("blue", 6)])
    c = Urn([("blue", 3), ("red", 3)])
    d = Urn([("blue", 1), ("red", 3), ("blue", 2)])
    print(c==d)
    print(c.balls)
    print(d.balls)
    print()
    a = Urn([("blue", 3), ("red", 3)])
    a.remove("red", 3)
    b = Urn([("blue", 3)])
    print(a==b)
    print(a.balls)
    print(b.balls)
    print(id(a))
    x=Urn([])
    print(x.balls)
    print()
    a = Urn([("blue", 1)])
    b = Urn([("blue", 1)])
    a.transfer(b)
    print(a.balls)
    print(b.balls)
    c = Urn([("blue", 2)])
    print(c)
    print(a==c)