'''Zadanie 3 (1 punkt). Szyfr Cezara2
to prosty sposób szyfrowania informacji. Zapoznaj się z nim
i napisz funkcję, która dla podanego ciągu znaków oraz klucza zwraca tekst zaszyfrowany tą metodą
dla wielkich liter alfabetu łacińskiego (pozostawiając pozostałe znaki w niezmienionej
postaci). Napisz również funkcję deszyfrującą.'''

'''letters=['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J' ,'K', 'L', 'M', 'N',
        'O', 'P', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
Len= len(letters) # 25'''

def Cezar_szyfruj(klucz, s):
    lst=[]
    for i in range (0, len(s) ):
        kod=ord( s[i] )
        if kod >=65 and kod <=90 :
            kod=kod+klucz
            while kod > 90: kod=kod-26
        lst.append(chr(kod))
    return "".join(lst)


def Cezar_rozszyfruj(klucz, s):
    lst=[]
    for i in range (0, len(s) ):
        kod=ord( s[i] )
        if kod >=65 and kod <=90 :
            kod=kod-klucz
            while kod < 65: kod=kod+26
        lst.append(chr(kod))
    return "".join(lst)


'''s="AAAAZZZBB"
szyf=Cezar_szyfruj(1, s)
print( szyf )
print( Cezar_rozszyfruj(1,szyf) )'''

t="ALA MA KOTA, a KOT ma ALĘ"
szyf=Cezar_szyfruj(3, t)
print( szyf )
print( Cezar_rozszyfruj(3,szyf) )