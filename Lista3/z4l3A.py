'''Zadanie 4 (1 punkt). Napisz funkcję totient(n), która dla dodatniej liczby naturalnej n
zwraca
∣{m ∈ N : m < n ∧ ∃k<n km ≡ 1(mod n)}∣
(jest to liczba elementów odwracalnych w zbiorze Zn z działaniem mnożenia modulo n)'''

def totient(n):
    ile=0
    for m in range (1,n):
        for k in range (0,n):
            if  (k*m) % n  == 1 :
                ile+=1
                break
    return ile


print(totient(4))
print(totient(5))
print(totient(1))