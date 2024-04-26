'''Zadanie 2 (1 punkt). Napisz program, który dla podanych czterech niezerowych liczb rze-
czywistych xa, ya, xb, yb rozstrzyga, czy punkty (xa, ya) i (xb, yb) znajdują się w tej samej
ćwiartce układu współrzednych'''

xa=float(input('xa='))
ya=float(input('ya='))
print('\n')
xb=float(input('xb='))
yb=float(input('yb='))
#w tej samej ćwiartce gdy współrzędne tego samego znaku, czyli ich iloczyn>0
if(xa*xb>0):
    if(ya*yb>0): print("Punkty w tej samej ćwiartce")
    else: print("Punkty w różnych ćwiartkach")
else: print("Punkty w różnych ćwiartkach")