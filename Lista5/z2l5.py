'''Zadanie 2 (1 punkt). Permutacją zbioru X nazywamy dowolną bijekcję f : X → X. Per-
mutację σ zbioru Xn = {0, 1, . . . , n − 1} można reprezentować jako listę lst długości n
taką2, że lst[i] = σ(i) dla wszystkich 0 <= i < n.
(1) (0,5 punktu) Napisz funkcję inverse(sigma), która dla listy sigma długości n repre-
zentującej permutację σ zbioru Xn zwraca listę reprezentującą permutację σ^(−1).
(2) (0,5 punktu) Napisz funkcję composition(sigma1, sigma2), która dla list sigma1,
sigma2 długości n reprezentujących odpowiednio permutacje σ1, σ2 zbioru Xn zwróci
listę reprezentującą permutację σ1 ◦ σ2.'''

def inverse(sigma):

    odp=[]
    i=0
    while( len(odp) != len(sigma) ):
       odp.append( sigma.index(i) )
       i=i+1

    return odp

print ( inverse([0,1,2,4,3]) )
print ( inverse([4,3,1,2,0]) )
print ( inverse([2,0,3,1]) )
print ( inverse([0,1,2]) )

def composition(sigma1, sigma2):
    if len(sigma1) != len(sigma2): return "BŁĄÐ"
    odp=[]
    i=0
    while (len(odp) != len(sigma1) ):
        odp.append(sigma1[ sigma2[i] ] )
        i = i + 1
    return odp

print(composition([0,2,1],[2,0,1]))