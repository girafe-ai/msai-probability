import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.arange(2,13)

y = np.concatenate((np.arange(1,7),np.arange(5,0,-1)))/36.

ax.stem(x,y,basefmt='white',linefmt='black',markerfmt='C3o')
ax.set_ylim(0,0.25)
ax.set_ylabel('PMF')
ax.set_xlabel('$T=X+Y$')

plt.savefig('two_dice_rolls_pmf.png',dpi=1200)