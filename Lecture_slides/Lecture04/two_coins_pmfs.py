import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)

fig.figsize=(5, 3)

x1 = [0,1,2]
y1 = [0.25,0.5,0.25]

ax1.stem(x1,y1,basefmt='white',linefmt='black',markerfmt='C3o')
ax1.set_xlim(-1,3)
ax1.set_ylim(0,1)
ax1.set_aspect(3.5)
ax1.set_xlabel('$X,Y$')
ax1.set_ylabel('PMF')

x2 = [0,1]
y2 = [0.5,0.5]

ax2.stem(x2,y2,basefmt='white',linefmt='black',markerfmt='C3o')
ax2.set_xlim(-1,3)
ax2.set_ylim(0,1)
ax2.set_aspect(3.5)
ax2.set_xlabel('$I$')

plt.savefig('two_coins_pmfs.png',dpi=1200)