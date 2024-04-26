'''Zadanie 2 (1 punkt).
(a) Napisz funkcję sum digits(n), która dla liczby naturalnej n zwraca sumę jej cyfr (w
zapisie dziesiętnym)1.
(b) Napisz funkcję is divisible3(n), która rozstrzyga (zwracając True lub False), czy
liczba naturalna n jest podzielna przez 3 z użyciem następującego (dobrze znanego)
rekurencyjnego schematu:
 Jeśli n jest jednocyfrowa, wtedy jest podzielna przez 3 gdy n ∈ {0, 3, 6, 9}.
 W przeciwnym wypadku, n jest podzielna przez 3 gdy suma jej cyfr jest podzielna
przez 3.'''

def sum_digits(n):
    suma = 0
    i = 0  # ktora cyfra od konca
    cyfra = 0
    while (n >= 10 ** i):
        cyfra = (int(n / 10 ** (i)) % 10)
        i += 1
        # print(cyfra)
        suma += cyfra
    return suma




def is_divisible3(n):
    if n<10 :
        if n in (0,3,6,9) : return True
        else: return False
    else:
        return is_divisible3( sum_digits(n) )

n = int( input ("Podaj n: ") )
print("Suma cyfr wynosi", sum_digits(n) )
print( is_divisible3(n) )