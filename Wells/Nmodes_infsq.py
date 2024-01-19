# IMPORT PACKAGES
import numpy as np
import numba # speed up summation
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
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
def myfigure():
    fig, ax = plt.subplots(1, 1, figsize = (8,6))
    plt.subplots_adjust(bottom=.18)
    ax.set_xlim(0, 1)
    ax.set_ylim(-2, 2)
    ax.set_title('First N modes')
    ax.set_xlabel("x'")
    ax.set_ylabel(r"$Re(\psi)$")
    ax_Nslid = plt.axes([.17, 0.07, .65, .03], facecolor='lightgoldenrodyellow')
    Nslid = Slider(ax_Nslid, label='N', valmin=1, valmax = 10, valinit = 5, valstep = 1)
    return fig, ax, Nslid

nx, N0 = 1000, 5
xf = np.linspace(0, 1, nx)
tf = np.linspace(0, 10, 500)

psi = lambda N, t: nmodes(nx, t, N)
#psif = psi(t)

def animate(tf, fig, ax, Nslid):
    l, = ax.plot(xf, psi(5, 0))
    plt.pause(0.005)
    i = 0
    while i <= len(tf):
        if i == len(tf):
            i = 0
        Ns = Nslid.val
        l.set_data(xf, psi(Ns, tf[i]))
        plt.pause(0.005)
        i = i + 1

fig, ax, Nslid = myfigure()
animate(tf, fig, ax, Nslid)

plt.show()
# If you want to stop the algorithm, close the plot window and Ctrl+C in the Terminal to KeyboardInterrupt