'''Zadanie 2 (1 punkt). Z rozwiązania poprzedniego zadania zaimportuj pod nazwą fib rec
funkcję wyznaczającą wyrazy ciągu Fibonacciego w sposób rekurencyjny2.
(a) Napisz funkcję time fib(n), która mierzy i zwraca czas działania funkcji fib rec(n).
(b) Napisz funkcję, która wypisuje na ekran kolejne ilorazy ti+1/ti dla i = 0, 1, . . ., gdzie
ti oznacza czas wykonania fib rec(i). Funkcja powinna skończyć działanie, gdy obli-
czony ti+1 przekracza 30 sekund.'''
from z1l4 import fibb_recursive as fib_rec
from time import perf_counter as perf

def time_fib(n):
    t0=perf()
    fib_rec(n)
    t1=perf()
    return (t1-t0)


n = int(input("n="))
print(time_fib(n))
#dla n=33 trwa >1sec
print('\n')

def ilorazy():
    n=25
    #  print("t"+n+" + t"+n+1+" =",iloraz)
    while ( time_fib(n + 1) < 30 ) :
    # while (time_fib(n + 1) < 30):
        iloraz = time_fib(n) / time_fib(n + 1)
        print(iloraz)
        n+=1

ilorazy()