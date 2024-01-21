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
def polyinfsq(nx, t, N, L=1) -> np.array: # nx = x array points ; N = numb. of oscillation modes
    x = np.linspace(0, L, nx)
    psir = np.zeros(nx)
    psii = np.zeros(nx)
    for n in range(1, N+1):
        for i in range(nx):
            psir[i] += -2*np.sqrt(2*105)*(1+2*(-1)**n)/np.pi**3/(n)**3*np.sqrt(2/L)*np.sin(np.pi*n*x[i]/L)*np.cos(((n)*np.pi)**2*t/L**2)
            psii[i] += -2*np.sqrt(2*105)*(1+2*(-1)**n)/np.pi**3/(n)**3*np.sqrt(2/L)*np.sin(np.pi*n*x[i]/L)*np.sin(((n)*np.pi)**2*t/L**2)
            # x, t rescaled [x/L , hbar * t / (2 * m)]
    return psir, psii


# ANIMATION

def myfigure():
    fig, ax = plt.subplots(1, 1, figsize=(6,5))
    plt.subplots_adjust(bottom=.3)
    ax.set_xlabel("x'")
    ax.set_title(r'Polynomial initial condition ($\propto x^2(1-x)$)')
    ax.set_xlim(0, 1)
    ax.set_ylim(-max(np.sqrt(105/L**7)*xf**2*(L-xf)), max(np.sqrt(105/L**7)*xf**2*(L-xf)))
    ax.grid()
    ax_Nslid = plt.axes([.2, 0.17, .65, .03], facecolor='lightgoldenrodyellow')
    Nslid = Slider(ax_Nslid, label='N', valmin=1, valmax = 10, valinit = 5, valstep = 1)
    return fig, ax, Nslid

nx, N, L = 1000, 7, 1
xf = np.linspace(0, L, nx)
tf = np.linspace(0, 10, 100)

psi = lambda t, N : polyinfsq(nx, t, N, L)

def animate(tf, fig, ax, Nslid):
    l1, = ax.plot(xf, psi(0, 5)[0], label=r'$Re(\psi(x,t))$')
    l2, = ax.plot(xf, psi(0, 5)[1], label=r'$Im(\psi(x,t))$')
    ax.legend(loc='upper right')
    plt.pause(0.005)
    i=0
    while i <= len(tf):
        if i == len(tf):
            i = 0
        Ns = Nslid.val
        l1.set_data(xf, psi(tf[i], Ns)[0])
        l2.set_data(xf, psi(tf[i], Ns)[1])
        plt.pause(0.0001)
        i = i + 1

fig, ax, Nslid = myfigure()
animate(tf, fig, ax, Nslid)

plt.show()

# If you want to stop the algorithm, close the plot window and Ctrl+C in the Terminal to KeyboardInterrupt