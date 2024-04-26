'''Zadanie 1 (1 punkt). Niech A będzie najmniejszą, a B największą dodatnią cyfrą Twojego indeksu.
Narysuj krzywą parametryczną zadaną wzorami'''

import matplotlib.pyplot as p
from math import sin, cos, pi
A=1; B=9

def x(t):
    return sin(t)+cos(A*t)/B

def y(t):
    return sin(B*t) + cos(A*A * t)

def frange(start,final,step=1):
    r=[]
    while(start<final):
        r.append(start)
        start=start+step
    return r

#p.plot([1,2,3])


ts=frange(0,2*pi,0.05)
xs=[]
ys=[]
for i in  range (0,len(ts)):
    t=ts[i]
    xs.append(x(t))
    ys.append(y(t))

        #ys = (y(t) for t in ts)
    #print(xs)
p.plot(xs,ys )
     #p.plot(ts, ys)
p.show()