import matplotlib.pyplot as plt
import numpy as np
from scipy.special import binom

x = np.arange(0,11)

def Bin(x,n,p):
    return binom(10,x) * (p**x) * (1-p)**(n-x)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.stem(x,Bin(x,10,0.5),basefmt='white',linefmt='black',markerfmt='C3o')
ax1.set_ylim(0,0.4)
ax1.set_xlim(0,10)
ax1.set_xticks([])
ax1.set_title('$Bin(10,1/2)$')

ax2.stem(x,Bin(x,10,1./8),basefmt='white',linefmt='black',markerfmt='C3o')
ax2.set_ylim(0,0.4)
ax2.set_xlim(0,10)
ax2.set_xticks([])
ax2.set_title('$Bin(10,1/8)$')

ax3.stem(x,Bin(x,10,1./3),basefmt='white',linefmt='black',markerfmt='C3o')
ax3.set_ylim(0,0.4)
ax3.set_xlim(0,10)
ax3.set_title('$Bin(10,1/3)$')

ax4.stem(x,Bin(x,10,4/5),basefmt='white',linefmt='black',markerfmt='C3o')
ax4.set_ylim(0,0.4)
ax4.set_xlim(0,10)
ax4.set_title('$Bin(10,4/5)$')

plt.savefig('binomial_pmfs.png',dpi=1200)