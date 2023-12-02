# IMPORT PACKAGES
import numpy as np
import numba # speed up summation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from matplotlib.widgets import Button
import scienceplots
njit = numba.njit 

plt.style.use(['science', 'no-latex'])

# FUNCTIONS
@njit
def polyinfsq(nx, t, N, L=1) -> np.array: # nx = x array points ; N = numb. of oscillation modes
    x = np.linspace(0, L, nx)
    psi = np.zeros(nx)
    for n in range(1, N+1):
        for i in range(nx):
            psi[i] += -2*np.sqrt(2*105)*(1+2*(-1)**n)/np.pi**3/(n)**3*np.sqrt(2/L)*np.sin(np.pi*n*x[i]/L)*np.cos(((n)*np.pi)**2*t/L**2)
            # x, t rescaled [x/L , hbar * t / (2 * m)]
    return psi


# ANIMATION
nx, N, L = 1000, 7, 1
t = np.linspace(0, 10, 100)

psi = lambda t, N : polyinfsq(nx, t, N, L)
#psif = psi(t)

'''fig, ax = plt.subplots(1, 1, figsize = (8,4))
l, = ax.plot([],[])
ax.set_xlim(0, 1)
ax.set_ylim(-2, 2)
ax.set_title(r'$\psi(x,0) = Ax(x-L)$')
ax.set_xlabel("x'")
ax.set_ylabel(r"$Re(\psi)}$")

def animate(i):
    l.set_data(np.linspace(0, 1, nx), psi(t[i]))
    return l,

ani = FuncAnimation(fig, animate, frames=len(t), interval=100)
plt.show()'''

fig, ax = plt.subplots(1, 1, figsize=(6,5))
plt.subplots_adjust(bottom=.3)

xf = np.linspace(0, L, nx)

l1, = ax.plot(xf, psi(0, 5))
l2, = ax.plot(xf, np.sqrt(105/L**7)*xf**2*(L-xf), '--', label=r'$\psi_0$')
ax.set_xlabel("x'")
ax.set_ylabel(r'$Re(\psi)$')
ax.set_title(r'Polynomial initial condition ($\propto x^2(1-x)$)')
ax.set_xlim(0, 1)
ax.set_ylim(-max(np.sqrt(105/L**7)*xf**2*(L-xf)), max(np.sqrt(105/L**7)*xf**2*(L-xf)))
ax.grid()
ax.legend()
ax_Nslid = plt.axes([.27, 0.17, .65, .03], facecolor='lightgoldenrodyellow')
ax_tslid = plt.axes([.27, 0.12, .65, .03], facecolor='lightgoldenrodyellow')
ax_button = plt.axes([.12, 0.125,.08, .08])
Nslid = Slider(ax_Nslid, label='N', valmin=1, valmax = 10, valinit = 5, valstep = 1)
tslid = Slider(ax_tslid, label='t (s)', valmin=0, valmax = 10, valinit = 0)
button = Button(ax_button, 'Pause')
button2 = ax_button.text(.5, .5, 'Play', verticalalignment='center', horizontalalignment='center', transform = ax_button.transAxes)
button2.set_visible(False)

class Buttonanimate:
    def toggle(self):
        def pause(event):
            if self._pause:
                self.event_source.start()
                self.button.set_visible(True)
                self.button2.set_visible(False)
            else:
                self.event_source.stop()
                self.button.set_visible(False)
                self.button2.set_visible(True)

            self.fig.canvas.draw()
            self._pause ^= True
        self.button.on_clicked(pause)

    def update(val):
        ts = tslid.val
        Ns = Nslid.val
        l1.set_xdata(xf)
        l1.set_ydata(psi(ts, Ns))
        fig.canvas.draw_idle()
    Nslid.on_changed(update)
    tslid.on_changed(update)
plt.show()