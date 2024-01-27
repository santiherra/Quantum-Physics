# IMPORT PACKAGES
import numpy as np
from scipy.special import jv
from scipy.special import jn_zeros
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import scienceplots

plt.style.use(['science', 'no-latex'])


# FUNCTIONS
w = 70  # We can set a proper frequency for illustrative purposes
def wavefunction(r, theta, t, m, l):
    n = np.abs(m)
    c = jn_zeros(n, l)[-1]  # L-th zero of the m-th Bessel function
    return jv(n, c*r)*np.cos(m*theta)*np.cos(w*t)


# ANIMATIONS
def myfigure():
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    plt.subplots_adjust(bottom=.18)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-.7, .7)
    ax.set_title('CIRCULAR INFINITE WELL')
    ax.set_xlabel("x/R")
    ax.set_ylabel("y/R")
    ax_Mslid = plt.axes([.22, 0.07, .65, .03], facecolor='lightgoldenrodyellow')
    ax_Lslid = plt.axes([.22, 0.02, .65, .03], facecolor='lightgoldenrodyellow')
    Mslid = Slider(ax_Mslid, label='m', valmin=0, valmax = 10, valinit = 0, valstep = 1)
    Lslid = Slider(ax_Lslid, label='l', valmin=1, valmax = 10, valinit = 0, valstep = 1)
    return fig, ax, Mslid, Lslid

r, the = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 2*np.pi, 100))
x, y = r*np.cos(the), r*np.sin(the)
tf = np.linspace(0, 2*np.pi, 1000)

psi = lambda m, l, t: wavefunction(r, the, t, m, l)

def animate(tf, fig, ax, Mslid, Lslid):
    ax.plot_surface(x, y, np.real(psi(0, 1, 0)), cmap='cool', edgecolor='k', linewidth=.2)
    plt.pause(0.5)
    i = 0
    while i <= len(tf):
        if i == len(tf):
            i = 0
        Ms = Mslid.val
        Ls = Lslid.val
        ax.clear()
        ax.plot_surface(x, y, np.real(psi(Ms, Ls, tf[i])), cmap='cool', edgecolor='k', linewidth=.2)
        ax.set_xlabel('x/R')
        ax.set_ylabel('y/R')
        ax.set_title('CIRCULAR INFINITE WELL')
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-.7, .7)
        plt.pause(0.5)
        i = i + 1

fig, ax, Mslid, Lslid = myfigure()
animate(tf, fig, ax, Mslid, Lslid)

plt.show()
# If you want to stop the algorithm, close the plot window and Ctrl+C in the Terminal to KeyboardInterrupt