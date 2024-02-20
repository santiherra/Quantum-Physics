# IMPORT PACKAGES
import numpy as np
import numba # speed up summation
from scipy.integrate import quad
from scipy.integrate import quad_vec
import matplotlib.pyplot as plt
import scienceplots
njit = numba.njit 

plt.style.use(['science', 'no-latex'])

# FUNCTIONS

def coeffs(f, N, L=1) -> np.array: # f = your desired function; N = number of terms ; L = well length
    n = np.linspace(int(1), int(N), int(N))
    g1 = lambda x: (f(x)*x*(L-x))**2
    I1 = quad(g1, 0, L)[0]
    g2 = lambda x, n: 1/np.sqrt(I1)*f(x)*x*(L-x)*np.sin(n*np.pi/L*x)*np.sqrt(2/L)
    I2 = quad_vec(g2, 0, L, args=(n,))[0]
    return I2

@njit
def polyinfsq(nx, t, N, C, L=1) -> np.array: # nx = x array points ; C = expansion coefficients
    x = np.linspace(0, L, nx)
    psir = np.zeros(nx)
    psii = np.zeros(nx)
    for n in range(1, N+1):
        for i in range(nx):
            psir[i] += C[n]*np.sqrt(2/L)*np.sin(np.pi*n*x[i]/L)*np.cos(((n)*np.pi)**2*t/L**2)
            psii[i] += C[n]*np.sqrt(2/L)*np.sin(np.pi*n*x[i]/L)*np.sin(((n)*np.pi)**2*t/L**2)
            # x, t rescaled [x/L , hbar * t / (2 * m)]
    return psir, psii


# ANIMATION

def myfigure():
    fig, ax = plt.subplots(1, 1, figsize=(6,5))
    plt.subplots_adjust(bottom=.3)
    ax.set_xlabel("x'")
    ax.set_title(r'Time evolution for initial distribution $\psi(x, 0) = f(x)x(L-x)$')
    ax.set_xlim(0, 1)
    ax.set_ylim(-max(np.sqrt(105/L**7)*xf**2*(L-xf)), max(np.sqrt(105/L**7)*xf**2*(L-xf)))
    ax.grid()
    return fig, ax

nx, L = 1000, 1
N = int(input('Number of terms: '))  # Recommended: around 10, for example for f(x) = x
L = int(input('Length of the well: '))
xf = np.linspace(0, L, nx)
tf = np.linspace(0, 10, 100)

fun = lambda x: x
C = coeffs(fun, N)
psi = lambda t, N : polyinfsq(nx, t, N, C, L)

def animate(tf, fig, ax):
    l1, = ax.plot(xf, psi(0, 5)[0], label=r'$Re(\psi(x,t))$')
    l2, = ax.plot(xf, psi(0, 5)[1], label=r'$Im(\psi(x,t))$')
    ax.legend(loc='upper right')
    plt.pause(0.005)
    i=0
    while i <= len(tf):
        if i == len(tf):
            i = 0
        l1.set_data(xf, psi(tf[i], N)[0])
        l2.set_data(xf, psi(tf[i], N)[1])
        plt.pause(0.0001)
        i = i + 1

fig, ax = myfigure()
animate(tf, fig, ax)

plt.show()

# If you want to stop the algorithm, close the plot window and Ctrl+C in the Terminal to KeyboardInterrupt