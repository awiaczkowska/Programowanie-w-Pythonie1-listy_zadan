'''Zadanie 1 (1 punkt). Napisz program, który dla podanej liczby rzeczywistej a > 0 będącej
długością krawędzi czworościanu foremnego obliczy i poda jego objętość oraz pole powierzch-
ni ścian.'''

a = float(input('Podaj dlugosc krawędzi czworościanu foremnego:'))
pole  = a * a * (3 ** 0.5) #pole calkoite
H = a * (6 ** 0.5 ) / 3 #wysokosc
Pp=a*a*(3**0.5)/4 #pole podstawy
V=1/3*Pp*H

print('\nPole całkowite wymosi',pole)
print('Objętość wynosi',V)

