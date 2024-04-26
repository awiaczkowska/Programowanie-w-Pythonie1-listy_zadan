'''Zadanie 3 (1 punkt). W pewnym fikcyjnym kraju, podatek dochodowy oblicza się z użyciem
następujących progresywnych stawek podatkowych1 (wszystkie kwoty wyrażone są w walucie
tego kraju):
1. Dochód do 8000 nie jest opodatkowany.
2. Dochód pomiędzy 8000 a 34500 jest obłożony podatkiem w wysokości 10%.
3. Dochód powyżej 34500 jest obłożony podatkiem w wysokości 24%.
Napisz program, który dla podanej kwoty dochodu (liczba rzeczywista) wyznacza podatek
do zapłacenia. Dla kwoty 44500 podatek wynosi 5050.'''

doch=float(input("Podaj dochód: "))
prog1 = 8000
prog2 = 34500
if(doch<=prog1): print("Podatek wynosi 0.")
else:
    if(doch<=prog2): print('Podatek wynosi ',(doch-prog1)*0.1,'.')
    else: print('Podatek wynosi ',(doch-prog2)*0.24+(prog2-prog1)*0.1,'.')
