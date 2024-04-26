'''Zadanie 3. Napisz program, który dla podanych liczb rzeczywistych A i B rozstrzyga, czy
zbiór na płaszczyźnie opisany równaniem Ax + By = 0 jest prostą

czyli czy nie zachodzi A=B=0'''
a=float(input("A="))
b=float(input("B="))

if (a==0 and b==0):
    print(str(a)+"*x"+str(b)+'*y=0', 'jest punktem (0,0)')
else: print(a+"x"+b+'y=0','jest prostą' )
