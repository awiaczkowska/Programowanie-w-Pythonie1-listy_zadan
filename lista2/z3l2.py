'''Zadanie 3 (1 punkt). Napisz program, który wypisuje tabelę konwersji gęstości z jednostek
układu SI na niestandardowe. W pierwszej kolumnie powinny znajdować się gęstości równe
0, 10, 20, . . . , 1000 kilogramów na metr sześcienny (kg/m3). W kolumnach drugiej i trzeciej
powinny znajdować się odpowiadające im gęstości wyrażone w odpowiednio:
 tonach metrycznych na cal* sześcienny (t/in3),
 funtach brytyjskich na stopę angielską sześcienną (lbm/f t3).
Kolumny tabeli powinny być wyrównane i poprawnie opisane.'''

k1, k2, k3 = "(kg/m^3)", "(t/in^3)", "(lb_m/ft^3)"
print(f"{k1:10}", f"{k2:10}", f"{k3:10}")
for i in range (0,101):
    kg=10*i #kg/m3

    #przeliczniki jednostka1_jednostka2
    t_kg = 1000
    cal_m=2.54*0.01

    funt_kg=0.45359237
    stopa_m=0.3048

    t_in3 = (kg/t_kg) / (1/cal_m)**3
    lb_ft = (kg/funt_kg) / (1/stopa_m)**3

    print(f"{kg:<10}", f"{round(t_in3,7):<10}",f"{round(lb_ft,7):<10}")



