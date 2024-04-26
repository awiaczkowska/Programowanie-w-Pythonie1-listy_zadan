"""Zadanie 2 (1 punkt). Run-Length Encoding
jest prostą metodą kompresji ciągu znaków. Polega ona
na zamianie każdego ciągu powtórzonych znaków na parę (znak, ilość kolejnych powtórzeń).
Napisz funkcję wykonującą kompresję zgodnie z powyższym algorytmem.
Napisz również funkcję wykonującą operację odwrotną (tj. dekompresję)."""


def RLE(s):
    lst = []
    i = 0
    while i < len(s):
        ile = 1

        while (s[i] == s[i + 1]):
            ile = ile + 1
            i = i + 1
            if i == len(s) - 1:
                break
        krotka = (ile, s[i])
        lst.append(krotka)
        #print(krotka)
        i = i + 1
        if i == len(s) - 1:
            krotka = (ile, s[i])
            lst.append(krotka)
            break

    return lst



def re_RLE(c):
    lst = []
    for i in range( 0, len(c) ):
        for j in range (0, c[i][1]):
            lst.append( c[i][0] )
    return lst

if __name__=="__main__":
    l=[('a',4), ("b",1), ('c',6)]
    a=re_RLE(l)
    print(a)
    l=('A','A','A','A','C','C')
    c=RLE(l)
    print(c)