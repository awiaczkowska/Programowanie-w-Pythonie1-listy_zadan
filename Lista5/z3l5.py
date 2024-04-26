'''Zadanie 3 (1 punkt) Napisz funkcję pearson corr(lst1, lst2), która dla niepustych list
liczb rzeczywistych lst1=[x0, x1, . . . , xn−1] i lst2=[y0, y1, . . . , yn−1] oblicza i zwraca ich
współczynnik korelacji Pearsona3 zdefiniowany wzorem:'''

def kreska(lista):
    i=0
    suma=0
    while ( i<len(lista) ):
        suma=suma+lista[i]
        i=i+1
    return suma/len(lista)




def pierwiastek_z_mianownika(lista):
    i = 0
    suma = 0
    while (i < len(lista) ):
        suma=suma+ (lista[i] - kreska(lista) )**2
        i=i+1
    return suma**(0.5)

def licznik(list1, list2):
    #if len(list1) != len(list2) or len(list1)==0 or len(list1)==0 : return "BŁĄÐ"
    i = 0
    suma = 0
    while (i < len(list1)):
        suma=suma+ (list1[i] - kreska(list1) ) * (list2[i] - kreska(list2) )
        i = i + 1
    return suma

def pearson_corr(list1, list2):
    #if len(list1) != len(list2): return "BŁĄÐ"
    return licznik(list1, list2)/ ( pierwiastek_z_mianownika(list1) * pierwiastek_z_mianownika(list2) )


print(pierwiastek_z_mianownika([2,2,1]))
print(pearson_corr([2,0],[4,5] ))