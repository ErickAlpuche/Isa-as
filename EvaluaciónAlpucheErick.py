import matplotlib.pyplot as plt
import numpy as np

plt.axis([-10,200,-10,200])
plt.axis('on')
plt.grid(True)
plt.title('Rotation')

x1=0
x2=100
y1=80
y2=0

plt.plot([x1,x1],[y1,y2],linewidth=1,color=(0,.2,.4))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(0,.2,.4))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(0,.2,.4))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(0,.2,.4))

x1=50
x2=150
y1=40
y2=120

plt.plot([x1,x1],[y1,y2],linewidth=1,color=(0,.2,.4))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(0,.2,.4))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(0,.2,.4))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(0,.2,.4))

xc=100
yc=80
r=20

p1=0*np.pi/180
p2 =360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp], color= (0,.2,.4),linewidth=1)
    xlast=xp
    ylast=yp

plt.show()