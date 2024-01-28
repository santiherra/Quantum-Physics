# IMPORT PACKAGES
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal
from matplotlib.animation import FuncAnimation
import scienceplots

plt.style.use(['science', 'no-latex'])


# FUNCTIONS
def potential(x, U0): 
    N = len(x)
    U = np.zeros(N)
    for i in range(N):
        if i>=int(N/2):
            U[i] = U0
    return U

def psinot(x, x0, k, sigma=1):  
    f = np.exp(-(x-x0)**2/sigma**2)*np.exp(1j*k*(x-x0)) # Wavepacket
    I = np.sum(np.abs(f)**2*(x[1]-x[0])) # Normalize
    return f/np.sqrt(I)


# ANIMATIONS
N = 1000
x = np.linspace(0, 12, N+1)
dx = x[1]-x[0]
k, x0, sigma = 30, 3, .5
U0 = k**2/2

U = potential(x[1:-1], U0)
psi0 = psinot(x[1:-1], x0, k, sigma)
plt.plot(x[1:-1], .003*U, label='$V(x)$')
plt.plot(x[1:-1], np.abs(psi0), label=r'$|\psi(x,0)|$')
plt.plot(x[1:-1], np.real(psi0), label=r'$Re(\psi(x,0))$')
plt.plot(x[1:-1], np.imag(psi0), label=r'$Im(\psi(x,0))$')
plt.title('Initial Wavefunction')
plt.legend()
plt.grid()

diagonal, offdiag = 1/dx**2*np.ones(N-1)+U, (-1/(2*dx**2))*np.ones(N-2)
E, phi = eigh_tridiagonal(diagonal, offdiag)
A = np.sum(np.abs(phi[:,0])**2*dx) # Amplitude square of the first eigenfunction, we just take this one for simplicity, as it is approximately equal for all eigenstates
phi = phi.T/np.sqrt(A) # Normalize the eigenfunctions in our domain

def psifun(t):
    c = 0*psi0  # Build the coefficients
    for i in range(0, N-1):
        c[i] = np.sum(np.conj(phi[i])*psi0*dx)    
    psif = phi.T@(c*np.exp(-1j*E*t)) # Total wavefunction
    return psif

fig, ax = plt.subplots(1, 1, figsize = (5,3))
ln1, = ax.plot([], [], label=r'$V(x)$')
ln2, = ax.plot([], [], label=r'$Re(\psi(x,t))$')
ln3, = ax.plot([], [], label=r'$Im(\psi(x,t))$')
ax.set_xlim(min(x),max(x))
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("x")
ax.grid()
ax.legend()
t = np.linspace(0, 0.25, 100)
n = len(t)

def animate(i): # Animation function
  ln1.set_data(x[1:-1], .003*U)
  ln2.set_data(x[1:-1], np.real(psifun(t[i])))
  ln3.set_data(x[1:-1], np.imag(psifun(t[i])))
  return ln1, ln2, ln3,

ani = FuncAnimation(fig, animate, frames=len(t), interval=30, blit=True)
plt.show()