'''Zadanie 4 (1 punkt). Napisz program, który dla zadanej dodatniej liczby naturalnej wyznacza
ilość jej naturalnych dzielników niepodzielnych przez 5.'''


n=int(input("Podaj dodatnia liczbe naturalna: "))
dzielniki=0 #;iczba dzielnikow
print("dzielniki to:")
for i in range (1,n+1):
    if(n%i==0 and n%5!=0):
        print(i)
        dzielniki+=1
print("Liczba",n, "ma",dzielniki,"dzielników.")
