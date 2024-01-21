# IMPORT PACKAGES
import numpy as np
from scipy.special import eval_hermite
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import scienceplots

plt.style.use(['science', 'no-latex'])

# FUNCTIONS

def modes(x, t, n, w=1):
    A = np.sqrt(np.sqrt(w)/2**n/np.math.factorial(n)/np.pi)  # Normalization constant
    f = A*eval_hermite(n, np.sqrt(w)*x)*np.exp(-w*x**2/2)  # Eigenstates of harmonic potential
    E = w*(n+1/2)  # Energy of the nth mode (divided by hbar)
    return f*np.cos(E*t)

# ANIMATIONS

x = np.linspace(-2.5, 2.5, 100)
w = 2
t = np.linspace(0, 5, 100)

def myfigure():
    fig, ax = plt.subplots(1, 1, figsize = (8,6))
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.yaxis.set_tick_params(labelleft=False)
    ax.set_yticks([])
    ax.plot(x, modes(x, 0, 0, w) + .75*np.ones(len(x)))
    ax.plot(x, modes(x, 0, 1, w) + 2.25*np.ones(len(x)))
    ax.plot(x, modes(x, 0, 2, w) + 3.75*np.ones(len(x)))
    ax.plot(x, modes(x, 0, 3, w) + 5.25*np.ones(len(x)))
    ax.plot(x, modes(x, 0, 4, w) + 6.75*np.ones(len(x)))
    ax.plot(x, .75*np.ones(len(x)), '--', color='grey')
    ax.plot(x, 2.25*np.ones(len(x)), '--', color='grey')
    ax.plot(x, 3.75*np.ones(len(x)), '--', color='grey')
    ax.plot(x, 5.25*np.ones(len(x)), '--', color='grey')
    ax.plot(x, 6.75*np.ones(len(x)), '--', color='grey')
    ax.plot(x, w**2*x**2/2, color='black', label=r'$V(x) = \frac{1}{2}m\omega^2 x^2$')
    ax.text(-3.1, .75, r'$E_0 = \frac{\hbar \omega}{2}$')
    ax.text(-3.1, 2.25, r'$E_1 = \frac{3\hbar \omega}{2}$')
    ax.text(-3.1, 3.75, r'$E_2 = \frac{5\hbar \omega}{2}$')
    ax.text(-3.1, 5.25, r'$E_3 = \frac{7\hbar \omega}{2}$')
    ax.text(-3.1, 6.75, r'$E_4 = \frac{9\hbar \omega}{2}$')
    ax.text(-1, 7.5, r'$(\omega = $'+str(w)+')')
    ax.set_ylim(0, 8)
    fig.suptitle('Quantum Harmonic Oscillator Eigenstates')
    plt.legend(bbox_to_anchor=(.8, 1))
    return fig, ax

def animation(t, fig, ax):
    l1, = ax.plot([], [], lw=.5)
    l2, = ax.plot([], [], lw=.5)
    l3, = ax.plot([], [], lw=.5)
    l4, = ax.plot([], [], lw=.5)
    l5, = ax.plot([], [], lw=.5)
    plt.pause(0.005)
    i = 0
    while i <= len(t):
        if i == len(t):
            i = 0
        l1.set_data(x, modes(x, t[i], 0, w) + .75*np.ones(len(x)))
        l2.set_data(x, modes(x, t[i], 1, w) + 2.25*np.ones(len(x)))
        l3.set_data(x, modes(x, t[i], 2, w) + 3.75*np.ones(len(x)))
        l4.set_data(x, modes(x, t[i], 3, w) + 5.25*np.ones(len(x)))
        l5.set_data(x, modes(x, t[i], 4, w) + 6.75*np.ones(len(x)))
        plt.pause(0.005)
        i = i + 1

fig, ax = myfigure()
animation(t, fig, ax)

plt.show()
# If you want to stop the algorithm, close the plot window and Ctrl+C in the Terminal to KeyboardInterrupt