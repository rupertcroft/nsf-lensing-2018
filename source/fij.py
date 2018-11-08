import numpy as np
import matplotlib.pyplot as plt

### the (S/N)^2 = \bar n \sum_{ij} (w'(\theta_{ij}) f_{ij})^2
### consider the signal to noise as a function of thmax
### Take w=A (1'/\theta) --> w' = A(1'/theta^2)
### Consider the sum for each i:
####  S_i = \sigma_j (w'(\theta_{ij}) f_{ij})^2
#### Then,
#####  (S/N)^2 = \bar n \sum_i S_i = \bar n \Delta^{-2} \int d^2\theta_i S_i
#### where now \bar n/\Delta^2 is the number of galaxies per pixel of size \Delta^2, call it np
#### So,
#####  (S/N)^2 = np 2\pi \int d\theta/\theta (\theta^2 S(theta)
##### A good sense of where the constraining power comes from is to take the average value in a given annulus
####  as a proxy for S and then look at the log plot of theta^2 S 
thetae=.5
thmax=1.25

def dtheta(x1,y1):
	theta2=(x1)**2+(y1)**2
	dtheta=(thetae**2/theta2)
	return dtheta*(x1),dtheta*(y1)	
	
def grid(thmax):
	x=np.arange(-thmax,thmax,.5)
	y = np.arange(-thmax,thmax,.5)
	n=np.size(x)
	n2=n**2
	xi=np.zeros(n2)
	yi=np.zeros(n2)
	for i in range(n2):
		imod=i
		if imod >= n:
			imod = i - n*(i/n)
		xi[i]=x[imod]
		jmod=(i/n)
		yi[i]=y[jmod]
	return xi,yi,n2
	
xi,yi,n2=grid(thmax)
f=0.
delta=[]
fp=[]
for i in range(n2):
	thetai=np.sqrt(xi[i]**2+yi[i]**2)
	dxi,dyi=dtheta(xi[i],yi[i])
	delta.append(thetai)
	sum=0.
	for j in range(i+1,n2):
		thetaij=np.sqrt(  (xi[i]-xi[j])**2 + (yi[i]-yi[j])**2 )
		dxj,dyj=dtheta(xi[j],yi[j])
		sum+= (  ((dxi-dxj)*(xi[i]-xi[j]) +  (dyi-dyj)*(yi[i]-yi[j]) )  /thetaij**3)**2
	fp.append(sum)
	f+=sum
print f
delta=np.array(delta)
fp=np.array(fp)
plt.scatter(delta,2*3.14159*delta**2*fp)
plt.xlabel('$\\theta (arcmin)$')
plt.ylabel('$(S/N)^2$')
plt.yscale('log')
plt.xscale('log')
plt.axis([0.2,5,0.01,100])
plt.savefig('fthij.pdf')
