import sympy as s

#a)
print("a)")
expr=s.E**(s.pi/s.E)
#s.pprint(s.pi.evalf(3))
print(expr.evalf(100)) #rozwiniecie do 100 cyfr znaczacych
print()
#b)
print("b)")
x=s.Symbol('x')
expr=x**4 + 5 * x**2 + 32 - 4 * x**3 - 104
print( s.solve(expr) )
print()
#c)
print("c)")
f = ( s.sin(2**x - 1) ) / x
print ("granica lewostronna:",s.limit(f, x, 0, dir="-"))
print ("granica prawostronna:",s.limit(f, x, 0, dir="+"))
print()

#d)
print("d)")
f=s.E**( -x** 2** x)
s.pprint(f)
print("druga pochodna f:")
s.pprint( s.diff(s.diff(f)) )
print(); print();print()

#e)
print("e)")
f=(x* s.E**x * s.sin(x) )
expr=s.integrate(f)
s.pprint(expr)
expr=s.simplify(expr)
s.pprint(expr)
print(); print();print()

#f)
print("f)")
t=s.Symbol('t')
f=1/(1-t**2+t**4)
s.pprint(f)
expr=s.integrate(f,(t,-s.oo,s.oo) )
s.pprint(expr)


