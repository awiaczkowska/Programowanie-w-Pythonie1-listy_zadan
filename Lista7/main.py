# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
from matplotlib import pyplot as plt
from math import sin, cos, pi

def polar_range(start,final,fun,r,step=0.1,v=0):
    lst=[]
    while(start<=final+step):
        lst.append(r*fun(start)-v)
        start+=step
    return lst

def circle(x,y,r):
    xs = polar_range(0, 2 * pi, cos, 2,v=1)
    ys = polar_range(0, 2 * pi, sin, 2,v=2)

    plt.plot(xs,ys)
    plt.grid()
    plt.show()

def circle(x,y,r):
    xs = polar_range(0, 2 * pi, cos, 2,v=1)
    ys = polar_range(0, 2 * pi, sin, 2,v=2)

    plt.plot(xs,ys)
    plt.grid()
    plt.show()

circle(1,1,2)