'''Zadanie 6. Napisz program, który dla podanych wartości kapitału początkowego, ilości ka-
pitalizacji w roku, oprocentowania rocznego oraz okresu depozytu obliczy kapitał końcowy
(tzw. procent składany).'''

K0=float(input('podaj kapit2ał początkowy:'))
r=int(input('podaj roczne oprocentowanie w %:'))
k=int(input('podaj liczbę kapitalizacj w roku:'))
n=int(input('podaj okres depozytu w latach:'))

print('kapitał końcow to',K0*(1+r/100/k)**(k*n))

