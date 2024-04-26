'''Zadanie 3 (1,75 punktu). W materiałach do listy znajdują się pliki placowki.csv i pracownicy.csv.
Pierwszy zawiera dane o placówkach (np. sklepach, magazynach, biurach) pewnej fikcyjnej firmy.
Każda jego linijka zawiera, oddzielone średnikami, dane pojedynczej placówki. Te dane to kolejno:
 numer placówki (liczba całkowita),
 nazwa miasta, w którym mieści się placówka,
 rok otwarcia placówki,
 dowolna ilość numerów identyfikacyjnych pracowników placówki.
Przykładowa linijka w pliku: 7;Szczecin;2012;84305;94173;56261;29490
Drugi z plików zawiera informacje o pracownikach firmy. Każda jego linijka opisuje jednego pra-
cownika, zawierając następujące, oddzielone średnikami dane:
 imię pracownika,
 nazwisko pracownika,
 numer identyfikacyjny pracownika,
 nazwa stanowiska, na jakim jest zatrudniony,
 rok zatrudnienia w firmie.
Przykładowa linijka w pliku: Kamil;L.;79074;magazynier;2010


Napisz program, który wczytuje dane z obu plików i zawiera następujące funkcje:
(i) branches with(pos) - zwraca posortowaną listę numerów placówek, zatrudniających co naj-
mniej jednego pracownika, którego stanowiskiem jest pos.
(ii) old employees() - zwraca posortowaną listę pracowników, którzy zostali zatrudnieni w firmie
w roku wcześniejszym niż w placówce, w której aktualnie pracują.
(iii) manager cities() - zwraca posortowaną listę miast, w których jest placówka zatrudniająca
co najmniej jedną osobę na stanowisku ’manager’.
Przykładowy test do tego zadania znajduje się w pliku test3.py.
Uwaga: Możesz założyć, że każdy pracownik jest zatrudniony w dokładniej jednej placówce'''

def branches_with(pos):
    with open('placowki.csv') as p:
        with open('pracownicy.csv')as w:

            with_pos=[]
            for line in w:
                pracownik=line.split(';')
                if pracownik[3] == pos: with_pos.append( pracownik[2] )
                #if len(with_pos) > 4: break

            #print (with_pos)
            branches=[]
            for line in p:
                plac = line.split(';')
                i=3
                while( i<len(plac) ):
                    if plac[i] in with_pos:
                        branches.append( int(plac[0]) )
                        #print(( int(plac[0]) ))
                        break
                    i+=1
            #print(branches)
            branches.sort()
            return branches


def old_employees():
    #słownik: klucz-index, wartosc- pracownicy
    #iteracja po placowkach: spr czy slownik od pracownika

    with open('placowki.csv') as p:
        with open('pracownicy.csv') as w:
            daty={}
            for line in w:
                pracownik=line.split(';')
                daty[ int(pracownik[2]) ] = int(pracownik[4])

            old=[]
            for line in p:
                plac = line.split(';')
                rok=int( plac[2] )
                for i in (3,len(plac) ):
                    if daty[ int(plac[i]) ]< rok : old.append( int(plac[i]) )





if __name__ == "__main__":
    print(branches_with('magazynier'))