# Черных Сергей М8О-305Б-20
# Написать программу, строящую полиномиальную кривую по заданным точкам.
# Обеспечить возможность изменения позиции точек и, при необходимости,
# значений касательных векторов и натяжения
# Вариант 10. B-сплайн. n =  6, k =  3. Узловой вектор равномерный.

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si
import seaborn as sns
from matplotlib.widgets import Slider


points = [[3, 0], [0, 1], [3, 2], [7, 3], [9, 4], [5, 5]]  # начальные значения
points = np.array(points)
x = points[:, 0]
t = points[:, 1]
axcolor = 'darkgrey'


def interpol():
    global x
    global t
    ipl_t = np.linspace(min(t), max(t), 100)
    x_tup = si.splrep(t, x, k=3)  # согласно данным определить гладкую сплайн апроксимацию степени к на интервале
    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl
    x_i = si.splev(ipl_t, x_list) # оценить B сплйан
    return [ipl_t, x_i]


def update0(val):  # изменение из-за первой точки 
    global x
    global cords
    amp = samp0.val
    x[0] = amp
    cords = interpol()
    l.set_ydata(cords[1])
    a.set_ydata(x)


def update1(val):  # изменение из-за второй точки
    global x
    global cords
    amp = samp1.val
    x[1] = amp
    cords = interpol()
    l.set_ydata(cords[1])
    a.set_ydata(x)

 
def update2(val):  # изменение из-за третьей точки 
    global x
    global cords
    amp = samp2.val
    x[2] = amp
    cords = interpol()
    l.set_ydata(cords[1])
    a.set_ydata(x)


def update3(val):  # изменение из-за четвертой точки
    global x
    global cords
    amp = samp3.val
    x[3] = amp
    cords = interpol()
    l.set_ydata(cords[1])
    a.set_ydata(x)


def update4(val):    # изменение из-за пятой точки
    global x
    global cords
    amp = samp4.val
    x[4] = amp
    cords = interpol()
    l.set_ydata(cords[1])
    a.set_ydata(x)


def update5(val):   # изменение из-за шестой точки
    global x
    global cords
    amp = samp5.val
    x[5] = amp
    cords = interpol()
    l.set_ydata(cords[1])
    a.set_ydata(x)

sns.set_style("darkgrid")  # seaborn только для красоты 
sns.axes_style("darkgrid")
sns.set_context("talk")

fig = plt.figure(figsize=[8, 8])
ax = fig.add_subplot(2, 1, 1)
a, = plt.plot(t, x, '-o', color='blue')  # построение ломанной  
cords = interpol()
l, = plt.plot(cords[0], cords[1], 'r')  # построение кривой
plt.xlim([min(t) - 0.5, max(t) + 0.5])
plt.ylim([-1, 11])
plt.gcf().canvas.manager.set_window_title("B-сплайн. n =  6, k =  3. Узловой вектор равномерный")
plt.title('B - Сплайн, n = 6, k = 3')

axamp0 = plt.axes([0.25, 0.30, 0.65, 0.03], facecolor=axcolor)
axamp1 = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
axamp2 = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
axamp3 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axamp4 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp5 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

samp0 = Slider(axamp0, 'точка 0', 0.0, 10.0, valinit=points[0][0])
samp1 = Slider(axamp1, 'точка 1', 0.0, 10.0, valinit=points[1][0])
samp2 = Slider(axamp2, 'точка 2', 0.0, 10.0, valinit=points[2][0])
samp3 = Slider(axamp3, 'точка 3', 0.0, 10.0, valinit=points[3][0])
samp4 = Slider(axamp4, 'точка 4', 0.0, 10.0, valinit=points[4][0])
samp5 = Slider(axamp5, 'точка 5', 0.0, 10.0, valinit=points[5][0])

samp0.on_changed(update0)
samp1.on_changed(update1)
samp2.on_changed(update2)
samp3.on_changed(update3)
samp4.on_changed(update4)
samp5.on_changed(update5)

plt.show()
