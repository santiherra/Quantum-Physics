# IMPORT PACKAGES
import numpy as np
import numba # speed up summation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
#import animatplot as amp
import scienceplots
njit = numba.njit 

plt.style.use(['science', 'no-latex'])

# FUNCTIONS
@njit
def nmodes(nx, t, N, L=1) -> np.array: # nx = x array points ; N = numb. of oscillation modes
    x = np.linspace(0, 1, nx)
    psi = np.zeros(nx)
    for n in range(1, N+1):
        for i in range(nx):
            psi[i] += np.sqrt(2/N)*np.sin(np.pi*n*x[i])*np.cos((n*np.pi)**2*t)
            # x, t rescaled [x/L , hbar * t / (2 * m)]
    return psi


# ANIMATION
nx, N0 = 1000, 5
xf = np.linspace(0, 1, nx)
t = np.linspace(0, 10, 100)

psi = lambda N, t: nmodes(nx, t, N)
#psif = psi(t)

fig, ax = plt.subplots(1, 1, figsize = (8,4))
l, = ax.plot([],[])
ax.set_xlim(0, 1)
ax.set_ylim(-2, 2)
ax.set_title('First N modes')
ax.set_xlabel("x'")
ax.set_ylabel(r"$Re(\psi)}$")
ax_Nslid = plt.axes([.27, 0.17, .65, .03], facecolor='lightgoldenrodyellow')
Nslid = Slider(ax_Nslid, label='N', valmin=1, valmax = 10, valinit = 5, valstep = 1)

def animate(i):
    def update(val):
        Ns = Nslid.val
        l.set_xdata(xf)
        l.set_ydata(psi(t[i], Ns))
        fig.canvas.draw_idle()
    Nslid.on_changed(update)
    return l,

ani = FuncAnimation(fig, animate, frames=len(t), interval=100)
plt.show()
