###################################################################
# Модель снижения сердечно-сосудистой смертности от снижения      #
# популяционного уровня систолического артериального давления     #
# Модель D-delta_sP                                               #
# D  - Death                                                      #
# sP  - delta systolic Pressure                                   #
# Andrey V Lazarev                                                #
###################################################################
import numpy as np
import matplotlib.pylab as plt
n = 120
deltaAD = np.linspace(-40, 0, n)

def decreaseAD(dAD):
    return 2**(dAD / 20)

decreaseDeath = decreaseAD(deltaAD)
fig, ax = plt.subplots(figsize=(7,5))
ax.plot(deltaAD, decreaseDeath, alpha=0.8, label=r"$y = e^{0,034657 \cdot \Delta sP}$")
ax.plot(deltaAD, np.ones(n), ls='--', label=r"исходный уровень риска смертности - 1.0")
ax.set_xlabel('Снижение популяционного уровня АД, мм рт. ст.')
ax.set_ylabel('Относительный уровень смерти от БСК')
ax.set_ylim(0, 1.19)
ax.legend(loc=2)
#ax.set_title('Зависимость относительного риска смерти при БСК от популяционного уровня артериального давления')
ax.grid(True)
plt.show()