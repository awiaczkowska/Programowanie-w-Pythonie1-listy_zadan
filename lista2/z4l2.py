'''Zadanie 4 (1 punkt). Napisz program, który dla wprowadzonego przez użytkownika ciągu
liczb rzeczywistych dodatnich wyznacza ich średnią geometryczną. Wprowadzanie ciągu
kończy się poprzez wprowadzenie napisu ’end’. Program powinien raportować błąd, jeśli
’end’ jest pierwszą podaną wartością'''

a = input("Wprowadź liczbę: ")
if (a == 'end'): print("Nie podałeś żadnych liczb")
else:
    ile=0
    iloczyn=1.0
    while(a!='end'):
    # if(a=='end'): break
        iloczyn*=float(a)
        ile+=1
        #print(iloczyn)
        a = input("Wprowadź liczbę: ")

    print("Średnia geometryczną podanych liczb wynosi", iloczyn ** (1/ile) )

