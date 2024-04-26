'''Zadanie 1 (1 punkt). Napisz program, który dla podanej liczby naturalnej n poda sumę jej
nieparzystych cyfr (w zapisie dziesiętnym).'''

n = int( input ("Podaj n: ") )
suma=0
i=0 #ktora cyfra od konca
cyfra=0
while ( n >= 10 ** i ) :
    cyfra = ( int(n / 10**(i) ) % 10 )
    i+=1
    #print(cyfra)
    if( cyfra % 2 == 1 ):
        suma+=cyfra
print("Suma nieparzystych cyfr wynosi",suma)

