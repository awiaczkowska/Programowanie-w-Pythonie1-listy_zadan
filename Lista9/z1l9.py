'''Zadanie 1 (1 punkt). Kosmita ma naturalną dodatnią liczbę oczu i naturalną dodatnią liczbę głów.
Uporządkowana para kosmitów (a, b) jest kompatybilna, gdy a ma więcej oczu niż b lub b ma więcej głów niż
a.
Jeśli para kosmitów (a, b) jest kompatybilna, kosmita a może zjeść kosmitę b, przejmując wszystkie jego
głowy (poza jedną) i jedno oko (chyba, że b ma tylko jedno).
 Kosmita o parzystej liczbie głów i oczu może
podzielić się na parę kosmitów o równych liczbach głów i oczu. Napisz klasę Alien służącą do reprezentacji
kosmitów, zawierającą następujące metody:
 init (self, eyes=1, heads=1) – inicjalizator tworzący kosmitę mającego eyes oczu i heads głów,
gdzie eyes i heads to naturalne liczby dodatnie.
 compatible with(self, other alien) – zwraca True, gdy para kosmitów (self, other alien) jest
kompatybilna.
 eat(self, other alien) – realizuje operację zjadania other alien przez self.
 divide(self) – zwraca parę kosmitów (instancji Alien) powstałych z podziału self. Jednym z ele-
mentów tej pary powinien być self, drugim nowa instancja Alien.
W każdej z tych metod rzuć wyjątek, gdyby metoda miała doprowadzić do nielegalnej sytuacji (np. gdyby
kosmita miał po podziale niecałkowitą liczbę głów).'''

class Alien:
    def __init__(self, eyes=1, heads=1):
        if eyes<=0 or heads<=0: raise ValueError("Podano niedodatni parametr!")
        self.eyes=int(eyes)
        self.heads=int(heads)

    def compatible_with(self, other_alien):
        if self.eyes > other_alien.eyes or other_alien.heads > self.heads : return True
        return False

    def eat(self, other_alien):
        if  (a1.compatible_with(other_alien) == False) : raise ValueError("Kosmici niekomaptybilni!") #to ten Error?

        glowy=other_alien.heads-1 #głowy które sa zjedzone
        self.heads+=glowy
        other_alien.heads-=glowy
        if other_alien.eyes>1:
            self.eyes+=1
            other_alien.eyes-=1

    def divide(self):
        if self.eyes % 2 != 0 or self.heads % 2 != 0: raise ValueError("Kosmita niepodzielny!")
        self.heads=int(self.heads/2)
        self.eyes = int(self.eyes / 2)
        return (self, Alien(self.eyes, self.heads) )

if __name__=="__main__":
    a1=Alien(8,4)
    a2=Alien(2,4)
    a3=Alien(1,1)
    print( a1.divide() )
    print(a1.eyes, a1.heads)
    a1.eat(a2)
    print(a1.eyes, a1.heads)
    a1.eat(a2)
    print(a1.eyes, a1.heads)
    #a3.eat(a1) #wyrzuca blad jak chcielismy

