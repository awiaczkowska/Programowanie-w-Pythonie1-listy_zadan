'''Zadanie 3 (1 punkt). Napisz funkcję print conversion table(start, step, count), któ-
ra wypisuje tabelkę jak w Zadaniu 3 z Listy 2 dla ciągu gęstości postaci start, start+step,
start+2step, . . ., step+(count−1)step.'''

def print_conversion_table(start, step, count):
    k1, k2, k3 = "(kg/m^3)", "(t/in^3)", "(lb_m/ft^3)"
    print(f"{k1:10}", f"{k2:10}", f"{k3:10}")
    for i in range(0, count+1):
        kg = start + step * i  # kg/m3

        # przeliczniki jednostka1_jednostka2
        t_kg = 1000
        cal_m = 2.54 * 0.01

        funt_kg = 0.45359237
        stopa_m = 0.3048

        t_in3 = (kg / t_kg) / (1 / cal_m) ** 3
        lb_ft = (kg / funt_kg) / (1 / stopa_m) ** 3

        print(f"{kg:<10}", f"{round(t_in3, 7):<10}", f"{round(lb_ft, 7):<10}")

print_conversion_table(100, 5, 7)