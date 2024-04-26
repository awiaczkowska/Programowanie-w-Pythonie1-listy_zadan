'''Zadanie 2 (1 punkt). Napisz program, który dla podanej dodatniej liczby naturalnej n i
liczby rzeczywistej x ∈ (−1, 1) wyznacza wartość wyrażenia
.'''
n = int( input ("Podaj n: ") )
x = float( input ("Podaj x: ") )
suma=0
for k in range(1,n+1):
    suma += - (-x)**k / k

print("Suma szeregu  wynosi",suma )