import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
im = image.imread('galaxycluster.png')
#fig, ax = plt.subplots()

a=.1
k=10.
plt.text(0,0,'*',fontsize=18)
x=np.arange(-1,1.,.0001)
y1=np.sqrt(1.-x**2)
y2=-y1
plt.plot(x,y1,'--k')
plt.plot(x,y2,'--k')
z1=y1*(1+a*np.sin(k*x))
z2=y2*(1+a*np.sin(k*x))
plt.plot(x,z1,'b')
plt.plot(x,z2,'b')
plt.axes().set_aspect('equal', 'datalim')
#plt.imshow(im, aspect='auto', extent=(-0.1, 0, -.4,-.5), zorder=-1)
plt.plot([-.15,0.04],[-.87,0.04])
plt.axis('off')
plt.savefig('td.pdf')
