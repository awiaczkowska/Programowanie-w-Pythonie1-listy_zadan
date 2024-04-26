'''Zadanie 1 (1 punkt). Ciąg Fibonacciego jest zdefiniowany poprzez
f0 = 0, f1 = 1,
fn = fn−1 + fn−2, (n ⩾ 2).
Napisz funkcje obliczające wartość fn trzema sposobami: iteracyjnie, rekurencyjnie (z uży-
ciem schematu powyżej), oraz z wykorzystaniem wzoru'''

def fibb_recursive(n):
    if n==0 : return 0
    elif n==1: return 1
    else: return fibb_recursive(n-1)+fibb_recursive(n-2)

def fibb_iteration(n):
    if n==0 : return 0
    elif n==1: return 1
    else:
        f0=0
        f1=1
        for _ in range (1,n):
            fn=f0+f1
            f0=f1
            f1=fn
        return fn



def fibb_formula(n):
    phi=0.5 * ( 1 + 5**0.5 )
    return int( phi**n / 5**0.5 + 0.5 )


'''while(True):
    n=1
    if fibb_iteration(n) != fibb_formula(n):
        print(n)
        break
    n+=1
    '''


'''while(True):
    n=70
    if fibb_iteration(n) != fibb_formula(n):
        if( fibb_iteration(n-1) == fibb_formula(n-1)): break
        else: n-=1
    n+=10'''


if __name__ == "__main__" :
    print("n=70")
    print(fibb_iteration(70))
    print(fibb_formula(70))

    print("n=71")
    print(fibb_iteration(71))
    print(fibb_formula(71))

    n = int(input("n="))
    print(fibb_recursive(n))
    print(fibb_iteration(n))
    print(fibb_formula(n))