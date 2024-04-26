'''Zadanie 4 (1 punkt) Wektory w przestrzeni Rn można reprezentować jako listy liczb rzeczy-
wistych długości n. Napisz funkcję add_vectors(w,v), która dla list w i v reprezentujących
wektory równej długości zwraca nową listę reprezentującą sumę tych wektorów.
Wskazówka: długość listy można zbadać tak, jak dla krotek lub napisów.'''

def add_vectors(w,v):
    if len(w)!=len(v):
        print ("ERROR")
        return None
    s=[]
    for i in range ( 0,len(w) ):
        s.append(w[i]+v[i])
    return s


w=[1,2];v=[3,4]
#print(w[1])
print (add_vectors(w,v))
