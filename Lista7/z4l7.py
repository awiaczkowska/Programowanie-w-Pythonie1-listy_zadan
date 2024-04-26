'''Zadanie 4 (1,25+0,25 punktu). Napisz funkcję draw shapes(file name), która rysuje kształty
 opisane w pliku o nazwie file_name. W każdej linijce pliku znajdują się dane oddzielone średnikami.
Pierwszą daną w linijce jest kształt, który linijka opisuje ("point", "circle" lub "rectangle"
oznaczające odpowiednio punkt, okrąg, i prostokąt; prostokąt jest bez wnętrza a jego odpowiednie
pary boków są równoległe do osi układu). Liczba kolejnych danych z linijki i ich znaczenie zależy
od opisanego kształtu:
 dla punktu: dwie liczby rzeczywiste opisujące kolejno jego współrzędne;
 dla okręgu: trzy liczby rzeczywiste opisujące kolejno współrzędne jego środka oraz promień;
 dla prostokąta: cztery liczby rzeczywiste opisujące kolejno współrzędne jego lewego dolnego
rogu i współrzędne prawego górnego rogu.
Okręgi przybliż używając krzywych łamanych. Przykładowym plikiem z danymi jest shapes.csv.
(część za 0,25 punktu) Zrób to zadanie w wersji, gdzie każda linijka może opcjonalnie zawierać dane o kolorze kształtu (napis rozpoznawany przez matplotlib). Kształty bez podanego koloru powinny być narysowane na czarno. Przykładowym plikiem z danymi dla tej wersji jest
shapes with colors.csv. Typowym efektem działania draw shapes dla przykładowych plików
jest shapes.png.
'''
import matplotlib.pyplot as plt
from math import sin, cos, pi

def polar_range(start,final,fun,r,step=0.1,v=0.0):
    lst=[]
    while(start<=final+step):
        lst.append(r*0.5*fun(start)+v)
        start+=step
    return lst

def draw_shapes(file_name):
    with open(file_name) as f:
        for line in f:
            if line.endswith('\n'): line=line[0:len(line)-1]
            obj=line.split(';')

           # plt.plot([-2,-1,0,1,2,3,4,5,6],[-2,-1,0,1,2,3,4,5,6], linestyle='-', linewidth=0)
            #coś jest nie tak z kolejnością w skalach

            if obj[0]=='point':
                x=[float( obj[1] )]; y=[float( obj[2] )]
                if len(obj)==3: obj.append("black")
                plt.plot(x, y, linestyle='None', marker='o', markersize=12, color=obj[3] )

            elif obj[0] == 'circle':
                X0 = float(obj[1]); Y0 = float(obj[2])
                x = polar_range(0, 2 * pi, cos, 2, v=X0)
                y = polar_range(0, 2 * pi, sin, 2, v=Y0)
                if len(obj) == 4: obj.append("black")
                plt.plot(x, y, linestyle='-', linewidth=3, color=obj[4])

            elif obj[0]=='rectangle':
                x1=float(obj[1]); y1=float(obj[2])
                x2=float(obj[3]); y2=float(obj[4])
                if len(obj) == 5: obj.append("black")
                plt.plot([x1,x2,x2], [y1,y1,y2], linestyle='-', linewidth=3, color=obj[5])
                plt.plot([x1,x1,x2], [y1,y2,y2], linestyle='-', linewidth=3, color=obj[5])


        plt.xscale('linear')
        plt.grid()
        #plt.yscale('linear')
        plt.show()

draw_shapes("shapes_with_colors.csv")

''' elif obj[0] == 'circle':
                print(obj)
                X0 = obj[1]; Y0 = obj[2]
                x = polar_range(0, 2 * pi, cos, 2, v=X0)
                y = polar_range(0, 2 * pi, sin, 2, v=Y0)
                if len(obj) == 4: obj.append("black")
                plt.plot(xs, ys,linestyle='-', linewidth=3, color=obj[4])'''