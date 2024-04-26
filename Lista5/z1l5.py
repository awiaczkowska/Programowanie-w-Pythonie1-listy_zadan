'''Zadanie 1 (0,5 punktu). Napisz funkcję is palindrome iter(it), która dla obiektu itero-
walnego it (reprezentującego skończony ciąg obiektów) sprawdza, czy jest on palindromem
(pierwszy jego element jest równy ostatniemu, drugi przedostatniemu, etc.). Nie zakładaj,
że it można indeksować1.'''

def is_palindrome(s):
    S_list=list(s)
    S_list_rev=S_list.copy()
    S_list.reverse()
    for i in range (0,  int(len(S_list)/2)  ):
        if (S_list[i] != S_list_rev[i] ): return False
    return True

s=iter(['a', [1,2], [1,2], 'a'])
print( is_palindrome(s) )