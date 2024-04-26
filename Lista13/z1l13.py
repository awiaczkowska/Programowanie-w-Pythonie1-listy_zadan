from matplotlib import pyplot as plt
from matplotlib import animation as ani
import math as m

def serce(xs,ys, n=1000):

    krok=(2*m.pi / n)
    for i in range (0, n+1):
        t=i*krok
        xs.append(m.cos(t) )
        ys.append(m.sin(t)+ abs( m.cos(t) )**0.5 )

def next_frame2(i,xs,ys):
    circle.center = (xs[i*10], ys[i*10])
    return circle,  # blit

def next_frame(i):
    circle.center = (xs[i*10], ys[i*10])
    return circle,  # blit
####################################################################

if __name__=="__main__":
    fig, axes=plt.subplots(2,2)
    #axes[0][0].set_aspect('equal')
    xs=[]; ys=[]
    serce(xs,ys,1000)
    axes[0][0].plot(xs,ys,color="magenta")

    circle = plt.Circle((xs[0], ys[0]), 0.05, color='b')
    axes[0][0].add_patch(circle)
    #anim = ani.FuncAnimation(fig, next_frame, frames=100, repeat=True, interval=1)
    anim = ani.FuncAnimation(fig, next_frame2, frames=100, repeat=True, interval=1, fargs=(xs,ys))
    ################################################################

def pierwsza(n):
    for i in range(2,int(n**0.5) ):
        if n%i==0: return False
    return True

def P(n=1000):
    lst=[]
    i=2
    ile=0
    while ile<n:
        if pierwsza(i):
            lst.append(i)
            ile+=1
        i+=1
    return lst

def f(n=1000):
    p=P(n)
    ys=[]
    for i in range( 1, len(p) ):
        b=(i+1) /m.log(i+1,m.e)
        ys.append( p[i] / b)
    return ys

if __name__ == "__main__":

    x2 = list(range(999))
    y2 = f(1000)
    axes[1][0].set(xlim=(0,1000),ylim=(0,60) )
    axes[1][0].plot(x2,y2)

############################################################
def fibb(n):
    lst = [0, 1]
    for i in range(2,n):
        lst.append( lst[i-1]+ lst[i-2] )
    return lst


if __name__ == "__main__":
    axes[0][1].plot(fibb(1000),color="darkviolet")
    axes[0][1].set(xlim=(-50, 1000))
    axes[0][1].set(yscale='log')
################################################################

def next_frame3(i):
    #i=10*j
    circle2.center = (5 + 2 * m.cos(i *  m.pi / 50), 5 + 2 *  m.sin(i *  m.pi / 50))
    circle2.radius = 2 + abs((i % 10) - 5) / 10
    color = (0, 0, abs( m.sin(i *  m.pi / 50)))
    circle2.set_color(color)
    circle2.set_alpha(abs( m.sin(i *  m.pi / 50)))

    rect.xy = (1 + i / 10, 1 + i / 10)
    rect.set_height(2 +  m.cos(i *  m.pi / 50))
    rect.set_width(1.5 +  m.sin(i *  m.pi / 50))
    rect.set_alpha(1 / 2 +  m.cos(i *  m.pi / 10) / 2)
    rect.angle = i

    return circle, rect


if __name__ == "__main__":
    circle2 = plt.Circle((5, 5), 2, color='b')
    rect = plt.Rectangle((1, 1), 1, 1, color='r', alpha=0.5)
    axes[1][1].set(xlim=(0, 11), ylim=(0, 11))
    axes[1][1].add_patch(circle2)
    axes[1][1].add_patch(rect)

    anim2 = ani.FuncAnimation(fig, next_frame3, frames=100, repeat=True, interval=100, blit=True)
    plt.show()