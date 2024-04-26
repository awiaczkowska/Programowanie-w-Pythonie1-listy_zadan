'''Zadanie 1 (1 punkt). Napis nazwiemy palindromem, jeśli po odczytaniu go wspak otrzymamy
ten sam napis. Napisz funkcję is palindrome(s), która dla napisu s zwraca True, jeśli s
jest palindromem, i False w przeciwnym wypadku.'''

def is_palindrome(s):
    for i in range (0,  int(len(s)/2)  ):
        if (s[i] != s[-i-1] ): return False
    return True

s=input()
print( is_palindrome(s) )