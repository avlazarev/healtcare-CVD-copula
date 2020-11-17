###################################################################
# Зависимость относительного риска сердечно-сосудистой смертности #
# от популяционного уровня систолического артериального давления  #
# Модель D-sP-Ch                                                  #
# D  - Death                                                      #
# sP  - systolic Pressure                                         #
# Andrey V Lazarev                                                #
###################################################################
import numpy as np
import matplotlib.pylab as plt

def risk(AD):
    return 2**((AD - 115) / 20)

X = np.linspace(100, 180, 81)
AD = np.arange(115,180,20)
Y = risk(X)
Y_AD = risk(AD)
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})
fig, ax = plt.subplots(figsize=(9,5))
ax.plot(X, Y, 'r', alpha=0.8, label=r"$y = 0,018581 \cdot e^{0,034657 \cdot sP}$")
ax.bar(AD,Y_AD, align="center", width=7, alpha=0.5)
ax.legend(loc=2)
ax.set_xlabel('Уровень АД, мм рт. ст.', fontsize=12)
ax.set_ylabel('Относительный риск смерти от БСК', fontsize=12)
#ax.set_title('Зависимость относительного риска смерти при БСК от популяционного уровня артериального давления')
ax.grid(True)
rects = ax.patches
labels = ["label%d" % i for i in range(len(rects))]
for rect, label in zip(rects, Y_AD):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 0.5, label,
            ha='center', va='bottom')
plt.show()