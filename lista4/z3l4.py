'''Zadanie 3 (1 punkt) Użyj funkcji gcd z wykładu (lub jej odpowiednika z modułu math) do
napisania funkcji simplify(p,q), która dla podanych liczb całkowitych p i q zwraca parę
(krotkę) liczb całkowitych p′, q′ taką, że:
 p′/q′ = p/q,
 p′/q′ jest ułamkiem nieskracalnym,
 q′ jest dodatnia.
Możesz założyć, że parametr q jest różny od 0'''

from math import gcd

def simplify(p,q): #q!=0
    g=gcd(p,q)
    if(q<0) :
        p=-p ; q=-q
    if g==1: return (p,q)
    else: return ( int(p/g) , int(q/g) )

p=int(input("p="))
q=int(input("q="))
print ( simplify(p,q) )

