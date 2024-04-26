'''Zadanie 4 (1,5 punktu). Użyj sita Eratostenesa45 do napisania funkcji get primes(n), która
dla liczby naturalnej n zwraca listę wszystkich liczb pierwszych mniejszych od n.'''
def get_primes(n):
    lst=list(range(n)) #liczymy od zera, ostatni element to n-1
    lst.remove(0) ; lst.remove(1)
    #print(lst)
    for dziel in lst  :
        #j= lst[ lst.index(dziel) +1 ] #znajdujemy pozycję dziel i usuwamy wielokrotności przechodzac od następnego wyrazu
        for j in lst:
            if lst.index(j) <=  lst.index(dziel) : continue
            if (j % dziel == 0):
                lst.remove(j)
            #print("j =", j)
        #print("dziel =",dziel)

    return lst

#lista=list(range(6))

print(get_primes(100))

