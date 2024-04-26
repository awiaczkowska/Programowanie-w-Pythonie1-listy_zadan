'''Zadanie 1 (0,75 punktu). Utwórz moduł z rozwiązania Zadania 2 z Listy 7. Następnie zaimpor-
tuj z niego funkcję kompresującą i użyj jej do napisania funkcji
compress file(input file, output file), która kompresuje zawartość pliku o nazwie input file
i zapisuje wynik w pliku o nazwie output file, umieszczając pary (znak, liczba wystąpień) w
osobnych linijkach, nie oddzielając znaku i liczby jego wystąpień (czyli linijka ’X10’ pliku wyjścio-
wego oznacza dziesięciokrotne wystąpienie ’X’).
Nieobowiązkowe: napisz też analogiczną funkcję dekompresującą podany plik.'''

from z2l7 import RLE
def compress_file(input_file, output_file):
    with open(input_file) as f:
        with open(output_file,"w") as o:
            for line in f:
                lst=list(line)
                rle=RLE(lst)

                for tup in rle:
                    a=str(tup[0]) ; b=str(tup[1])
                    o.write(a); o.write(b) ; o.write('\n')



if __name__ == "__main__":
    compress_file("kompresja", "plik_po_kompresji")