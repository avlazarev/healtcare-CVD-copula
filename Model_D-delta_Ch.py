
###################################################################
# Модель снижения сердечно-сосудистой смертности от снижения      #
# популяционного уровня холестерина (ЛПНП)                        #
# Модель D-delta_sP                                               #
# D  - Death                                                      #
# sP  - delta systolic Pressure                                   #
# Andrey V Lazarev                                                #
###################################################################
import numpy as np
import matplotlib.pylab as plt

def decreaseChol(deltaChol):
    d = 2**(deltaChol/43.3)
    return d

n = 120
deltaChol = np.linspace(-120, 0, n)
decreaseDeath = decreaseChol(deltaChol)
fig, ax = plt.subplots(figsize=(9,6))
ax.plot(deltaChol, decreaseDeath, alpha=0.8, label=r"$y = e^{0,03231 \cdot \Delta Ch}$")
ax.plot(deltaChol, np.ones(n), ls='--', label=r"исходный уровень риска смертности - 1.0")
ax.set_xlabel('Снижение популяционного уровня ЛПНП, мг/дл')
ax.set_ylabel('Относительный уровень смертности от БСК')
#ax.set_title('Зависимость относительного риска смерти при БСК от популяционного уровня холестерина (ЛПНП)')
ax.grid(True)
ax.set_ylim(0, 1.19)
ax.legend(loc=2)
plt.show()