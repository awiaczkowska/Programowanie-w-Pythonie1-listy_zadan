'''Zadanie 1 (0,5 punkt). W pliku collins2015.txt znajdują się słowa języka angielskiego (po jednym
na linijkę, zapisane wielkimi literami). Napisz program, który przepisze do pliku palindromes.txt
te słowa, które są palindromami.'''

def is_palindrome(s):
    for i in range (0,  int(len(s)/2)  ):
        if (s[i] != s[-i-1] ): return False
    return True

with open('collins2015.txt') as col:
    lst=[]
    for line in col:
        #line=col.readline()
        line=line[0:len(line) - 1] #usuwamy enter
        #print(is_palindrome(line) )
        #print(line+'o')
        if is_palindrome(line):
            #print(line)
            lst.append(line)
    print (lst)


