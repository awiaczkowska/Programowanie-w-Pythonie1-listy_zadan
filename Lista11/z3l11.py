import sympy as s

def najblizej (t,X,Y,x0,y0):
    '''t-symbol (rzeczywisty),
    X(t), Y(t) - wspolrzedne opisujace krzywa
    (x0,y0) - plt spoza krzywej'''
    x,y,a,b = s.symbols('x y a b')

    odleglosc1 = s. sympify( '(( x-a)**2 + (y-b)**2 ) **(0.5)' )#poitrzebujemy minimum z tego
    odleglosc2 = s.sympify('(( x-a)**2 + (y-b)**2 )') ##alternatyewnie mozn znalezc minimum tego

    F = odleglosc2.subs({a: x0, b: y0, x: X, y: Y})
    #s.pprint(F)
    ##szukamy minum fkcji F, 1 pochodna == 0
    dF_dt = s.diff(F, t)
    #s.pprint(dF_dt)
    F1=s.solve(dF_dt, dict=True) #mozliwe t
    #s.pprint(F1)
    F3=s.diff(F, t,t,t)

    F2 = s.diff(F, t, t)
    F3 = s.diff(F, t, t, t)
    #s.pprint(F2)

    for i in range(0,len(F1)):
        T0 = F1[i][t] #kandydat na t
        T={} #slownik tych kandydatow
        #print(F2.subs(t, T))
        T[T0]= F.subs(t,T0)

    #print(T)

    val=min(T.values())
    for key in T:
        if T[key]==val:
            T0=key
            break

    #print(val)
    #print(T0)
    return X.subs(t, T0), Y.subs(t, T0)
    '''
    T0 = F1[0][t]
    # s.pprint(T)
    

    odleglosc = odleglosc2.subs({a:x0, b:y0})
    s.pprint (odleglosc)

    #potrzebujemy znalezc minimum funkcji
    #minimum jest wtedy gdy pochodna odleglosci jest rowna 0

    dx=s.diff(odleglosc,x)
    dy=s.diff(odleglosc,y)

    expr_x_t = dx.subs(x, X)
    expr_y_t = dy.subs(y, Y)

    expr_x=s.solve(expr_x_t,t)
    expr_y = s.solve(expr_y_t,t)
    s.pprint(expr_x)
    s.pprint(expr_y)
    print()

    F=odleglosc.subs({x:Y, y : Y})
    s.pprint(F)


    #dF/dt = dF/dx * dx/dt + dF/dy * dy/dt
    dF_dt = s.diff(F, t)
    s.pprint(dF_dt)
    dx_dt = s.diff(X,t)
    dy_dt = s.diff(Y, t)
    print()
    expr=s.solve(dF_dt - x* dx_dt - y*dy_dt,t)
    s.pprint(expr)
    expr1=expr[0].subs({x:X, y:Y})
    s.pprint(expr1)
    wyrX=X.subs({t:expr1})
    wyrY =  Y.subs({t:expr1})
    #pochodna zero
    pochdnaX = s.diff(wyrX,t)

    s.pprint(s.solve(pochdnaX ))'''
    '''s.pprint(expr_x_t)

    expr=s.solve([dx,dy],t)'''

    #korzystamy z reg lancucha
    #dt= (dx * s.diff(X,t) + dt * s.diff(Y,t))

    #Rozw=s.solve(dt)
    #s.pprint(Rozw)

    #D1=d1.subs(x,X)
    #s.pprint( s.solve(d1,x,dict=True) )

if __name__=="__main__":
    #print("tu")
    t=s.Symbol('t',real=True)
    print(najblizej(t, t, (t-1)**2, 1, 1))
    print()

    print(najblizej(t, t, s.sympify(7), 1, 0))
    print()

    print(najblizej(t, s.sin(t), s.cos(t), 1,1 ))
    print()

    print(najblizej(t, t**2, t, 1, 0))
    print()
