'''Zadanie 3 (1,5 punktu). Napisz klasę Rectangle służącą do reprezentującji domkniętych prostokątów na
płaszczyźnie (którego boki są równoległe do osi układu), zawierającą następujące metody:
 init (self, x1, y1, x2, y2) – inicjalizator tworzący prostokąt, którego lewy dolny wierzchołek
to punkt (x1, y1), a prawy górny wierzchołek to (x2, y2).
 circumference(self) – zwraca obwód prostokąta self.
 area(self) – zwraca pole prostokąta self.
 intersects(self, other rectangle) – Zwraca True, jeśli prostokąt self przecina prostokąt other rectangle
i False w przeciwnym wypadku.
 contains(self, other rectangle) – zwraca True, jeśli prostokąt other rectangle zawiera się w
prostokącie self, False w przeciwnym wypadku.
 contained in(self, other rectangle) – zwraca True, jeśli prostokąt self zawiera się w prostokącie
other rectangle, False w przeciwnym wypadku.
 (za 0,25 punktu) draw(self) – rysuje i wyświetla prostokąt self z użyciem biblioteki matplotlib.'''

from matplotlib import pyplot as plt

def poz_odc(A1,A2,B1,B2): #fkcja zwraca pozycje odcinków
        if (A1==B1 and A2==B2) : return "pokrycie"
        if (A1<=B1 and A2<=B2) :
            if A2<=B1: return "rozlacne"
            else : return "naprzemian"
        if (B1<=A1 and B2<=A2) :
            if B2<=A1: return "rozlacne"
            else: return "naprzemian"
        if A1<=B1 and A2>=B2   : return "B w A"
        if (B1 <= A1 and B2>= A2): return 'A w B'

class Rectangle:
    def __init__(self ,x1, y1, x2, y2):
        if x2<=x1 or y2<=y1 : raise ValueError("Dlugosc boku musi byc dodatnia!")
        self.x1=x1 ; self.x2=x2
        self.y1=y1 ; self.y2=y2


    def h_len(self):
        return self.x2-self.x1

    def v_len(self):
        return self.y2-self.y1

    def circumference(self):
        return 2 * (self.h_len() + self.v_len() )

    def area(self):
        return self.h_len() * self.v_len()

    def intersects(self, other_rectangle):
        pozX=poz_odc(self.x1, self.x2 , other_rectangle.x1, other_rectangle.x2)
        pozY=poz_odc(self.y1, self.y2 , other_rectangle.y1, other_rectangle.y2)

        if (pozX == 'rozlaczne' or pozY == 'rozlaczne'): return False
        if pozY == "A w B" and pozX == "A w B": return False
        if pozY == "B w A" and pozX == "B w A": return False

        #tego co ponizej chyba nie trzeba pisac jesli wyzej uwzglednimy war o pokryciu
        if (pozX=="naprzemian" and pozY!='rozlaczne' ): return True
        if (pozY == "naprzemian" and pozX != 'rozlaczne'): return True

        if pozX=="pokrycie" and pozY!='rozlaczne' : return True
        if pozY == "pokrycie" and pozX != 'rozlaczne': return True

        if pozX=="A w B" and pozY=="B w A" : return True
        if pozY == "A w B" and pozX == "B w A": return True

    def contains(self, other_rectangle):
        warX = ( poz_odc(self.x1, self.x2, other_rectangle.x1, other_rectangle.x2)=="B w A" )
        warY = (poz_odc(self.y1, self.y2, other_rectangle.y1, other_rectangle.y2) == "B w A")
        return warX and warY

    def contained(self, other_rectangle):
        warX = ( poz_odc(self.x1, self.x2, other_rectangle.x1, other_rectangle.x2)=="A w B" )
        warY = (poz_odc(self.y1, self.y2, other_rectangle.y1, other_rectangle.y2) == "A w B")
        return warX and warY

    def draw(self, col="black"):
        x1=self.x1
        x2 = self.x2
        y1=self.y1
        y2 = self.y2
        plt.plot([x1, x2, x2], [y1, y1, y2], linestyle='-', linewidth=2, color=col)
        plt.plot([x1, x1, x2], [y1, y2, y2], linestyle='-', linewidth=2, color=col)
        plt.show()

if __name__=="__main__":
    r=Rectangle(0,0,2,1)
    c=Rectangle(-1,-1,4,4)
    d=Rectangle(1,2,4,7)
    print( r.circumference() )
    print(r.area() )
    print(r.contains(c))
    print(r.contained(c))
    c.draw()
    #d.draw()
    #r.draw()

