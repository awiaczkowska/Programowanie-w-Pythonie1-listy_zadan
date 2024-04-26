import sympy as s
from matplotlib import pyplot as plt
from random import uniform
'''Zadanie 1 (1 punkt). Niech
 A to koło o środku (5, 5) i promieniu 3,
 B to trójkąt o wierzchołkach (2, 1),(6, 2) i (7, 9),
oraz niech X to różnica symetryczna A i B (czyli zbiór punktów, które należą 
do dokładnie jednego z tych dwóch zbiorów). Przybliż eksperymentalnie pole zbioru X.
Wskazówka: uogólnij sposób przybliżania wartości π z wykładu.
'''
def czy_A(x,y): #czy punkt jest w A
    return (x-5)**2 + (y-5)**2 <= 9


def prosta (x,x1,y1,x2,y2):
    'x - symbol; funkcja zwraca prosta przez 2 punkty :(y=) ax+b'
    dx=x2-x1
    dy=y2-y1
    a=s.sympify(dy/dx)
    expr=(a * x1 + x - y1)
    B=s.solve([a*x1+x-y1 , a*x1+x-y1],x)
    b=B[x]
    #print(b)
    return a*x+b


def czy_B(X,x,y): #czy punkt jest w B
    'X - symbol'
    a= y>=prosta(X,2,1,6,2).subs(X,x)
    b= y<=prosta(X,2,1,7,9).subs(X,x)
    c= y>=prosta(X,6,2,7,9).subs(X,x)
    return (a and b and c)



def MonteCarlo(x,y,n=100):
    'x - symbol'
    assert n>0
    # 2 <= x <= 8       1 <= y <= 9 #pole prostokata to 6*8=4
    pole = 42

    a = 0; b = 0;  ab = 0;  none = 0
    ax=[];ay=[]; bx=[];by=[];  abx=[]; aby=[];  nx=[]; ny=[]
    for _ in range(0,n):
        X = uniform(2, 8)
        Y = uniform(2, 9)
        A=czy_A(X,Y) ; B=czy_B(x,X,Y)

        if(A and B):
            ab+=1
            abx.append(X)
            aby.append(Y)
        elif(A and not B):
            a += 1
            ax.append(X)
            ay.append(Y)
        elif(not A and B):
            b += 1
            bx.append(X)
            by.append(Y)

        else:
            none+=1
            nx.append(X)
            ny.append(Y)

    plt.scatter(abx,aby,c="magenta", s=1)
    plt.scatter(ax, ay, c="pink", s=1)
    plt.scatter(bx, by, c="blue", s=1)
    plt.scatter(nx, ny, c="yellow", s=1)
    plt.show()

    return(pole*ab/n)



if __name__=="__main__":
    x, y = s.symbols('x y')
    '''plt.plot([2,6,7,2],[1,2,9,1])#B
    a=prosta(x,2,1,7,9)
    plt.plot([1,2,3],[a.subs(x,1) ,a.subs(x,2) , a.subs(x,3)])
    plt.show()'''
    #print( MonteCarlo(x, y, 100) )
    print(MonteCarlo(x, y, 10000))