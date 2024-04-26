'''Zadanie 2 (1,5 punktu). Dla dostatecznie dużego tekstu, język w którym został on napisany można
odgadnąć na podstawie częstotliwości występujących w nim liter. Przykładowo, trzy najczęstsze
litery w języku angielskim (zaniedbując ich wielkość) to odpowiednio e, t, a; natomiast w języ-
ku polskim są to odpowiednio a, i, e.

Napisz funkcję guess language(input file, languages),
gdzie input file to nazwa pliku zawierającego tekst w nieznanym języku, a languages to słownik,
którego kluczami są napisy – nazwy języków, a wartościami trójki najpopularniejszych liter tego
języka. Zadaniem funkcji jest odgadnięcie (na podstawie słownika languages) języka, w którym
został napisany tekst i zwrócenie jego nazwy. Jeśli języka nie da się ustalić, funkcja powinna zwra-
cać napis "unknown".
Przykładowy test do tego zadania znajduje się w pliku test2.py.'''

def dict_index (d,val):
    for k in d:
        if d[k]==val :
            #print(k)
            return k



'''def guess_language_fail(input_file, languages):
    with open (input_file) as f:
        licznik={}
        for key in languages:
            licznik [key]=0 #tworzymy licznik slow, w formie slownika
        for line in f:
            for char in line:
                for key in languages:
                    if char in languages[key]: licznik [key]+=1

        lst = list(licznik.values())
        #print(lst)
        MaxVal=max(lst)

        #print("MaxVal index: ",dict_index(licznik, MaxVal))
        #print(lst.count(MaxVal))
        if lst.count(MaxVal) == 1: return dict_index(licznik, MaxVal)
        else : return 'unknown'
        
DZIAŁA DLA ZNANYCH JEZYKOW
'''


def guess_language(input_file, languages):
    with open(input_file,encoding='utf8') as f:
        literki={}
        for line in f:
            for char in line:
                if char.isalpha():
                    char=char.lower()
                    if char not in literki : literki[char]=1
                    else: literki[char]=1+literki[char]
        krotka=[]

        for _ in range(0,3):
            lst = list(literki.values())
            MaxVal=max(lst)
            krotka.append( dict_index(literki, MaxVal) )
            #print (dict_index(literki, MaxVal))
            del literki[dict_index(literki, MaxVal) ]
            #print('wykonalo sie')

        krotka=tuple(krotka)
        for k in languages:
            if krotka == languages[k]: return k

        #print(krotka)
        return 'unknown'







if __name__=='__main__':
    languages = {'english': ('e', 't', 'a'),
                 'spanish': ('e', 'a', 'o'),
                 'polish': ('a', 'i', 'e')}
    print(guess_language('german.txt', languages))

    '''d={1: 'a', 2:'b', 3:'c'}
    print(dict_index(d , 'c'))'''
    print (" ".isalpha())
    print("n".isalpha())