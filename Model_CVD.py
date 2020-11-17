#####################################################
# Концепция снижения сердечно-сосудистой смертности #
# Модель D-AP-Ch                                    #
# D  - Death                                        #
# A  - Arterial Pressure                            #
# Ch - Cholesterol                                  #
# Lazarev Andrey                                    #
#####################################################

import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

def decreaseAD(deltaAD):
    return 2**(deltaAD / 20)

def decreaseChol(deltaChol):
    return 2**(deltaChol/43.3)

def decreaseDeath(dAD, dCh):
    return decreaseAD(dAD)*decreaseChol(dCh)

#n = 120
deltaAD   = np.linspace(-40, 0, 120)
deltaChol = np.linspace(-120, 0, 120)

X,Y = np.meshgrid(deltaAD, deltaChol)
Z = decreaseDeath(X,Y)
fig = plt.figure(figsize=(9,9))
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.3, cstride=8, rstride=8)
cset = ax.contour(X, Y, Z, zdir='z', cmap=cm.coolwarm, offset=-0.15)#
cset = ax.contour(X, Y, Z, zdir='x',  cmap=cm.coolwarm, offset=-0.15)
cset = ax.contour(X, Y, Z, zdir='y',  cmap=cm.coolwarm, offset=-0.15)
ax.set_xlabel('Снижение АД, мм рт. ст.')
ax.set_xlim(-40, 0)
ax.set_ylabel('Снижение ЛПНП-ХС, мг/дл')
ax.set_ylim(-120, 0)
ax.set_zlabel('Уровень предотвратимых сердечно-сосудистых событий')
ax.set_zlim(-0.15, 1)
plt.show()

# Вариант 2
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0, cmap='jet', alpha=0.5)
cset = ax.contour(X, Y, Z, zdir='z', cmap=cm.coolwarm, offset=-0.15)
cset = ax.contour(X, Y, Z, zdir='x', cmap=cm.coolwarm, offset=-0.15)
cset = ax.contour(X, Y, Z, zdir='y', cmap=cm.coolwarm, offset=-0.15)
ax.set_xlabel('Снижение АД, мм рт. ст.')
ax.set_xlim(-40, 0)
ax.set_ylabel('Снижение ЛПНП-ХС, мг/дл')
ax.set_ylim(-120, 0)
ax.set_zlabel('Уровень предотвратимых сердечно-сосудистых событий')
ax.set_zlim(-0.15, 1)
plt.show()

#Z = 10.0 * (Z2 - Z1)
clev = np.arange(Z.min(),Z.max(),.1) #Adjust the .001 to get finer gradient
#CS = plt.contourf(X, Y, Z, clev, cmap=plt.cm.coolwarm)
plt.show()
fig, ax = plt.subplots(figsize=(9,6))
cset = ax.contour(X, Y, Z, clev,  cmap=cm.coolwarm)# zdir='y', offset=0
ax.set_xlabel('Снижение АД, мм рт. ст.')
ax.set_xlim(-40, 0)
ax.set_ylabel('Снижение ЛПНП-ХС, мг/дл')
ax.set_ylim(-120, 0)
plt.show()

fig, ax = plt.subplots(figsize=(9,6))
dec = np.arange(0,1, 0.1)
Con = plt.contour(X, Y, Z, dec)# , offset=0
CLabels = plt.clabel(Con, inline=1, fontsize=10)
ratio = 0.05
Xmin,Xmax,Ymin,Ymax = plt.axis()
Dx = Xmax-Xmin
Dy = Ymax-Ymin
labels = []
for label in CLabels:
    lx,ly = label.get_position()
    if Xmin + ratio * Dx < lx < Xmax - ratio * Dx and Ymin + ratio * Dy < ly < Ymax - ratio * Dy:
        labels.append((lx,ly))
ax.set_xlabel('Снижение АД, мм рт. ст.')
ax.set_xlim(-40, 0)
ax.set_ylabel('Снижение ЛПНП-ХС, мг/дл')
ax.set_ylim(-120, 0)
plt.show()