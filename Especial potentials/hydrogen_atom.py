# IMPORT PACKAGES
import numpy as np
from scipy.special import sph_harm
from scipy.special import assoc_laguerre
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import scienceplots

plt.style.use(['science', 'no-latex'])


# FUNCTIONS
def radialfunc(r, n, l):
    rho = 2*r/n  # Reduced radius, in atomic units
    normconst = np.sqrt((2/n)**3*np.math.factorial(n-l-1)/2/n/np.math.factorial(n+l))  # Normalization constant
    return normconst*np.exp(-rho/2)*rho**l*assoc_laguerre(rho, n-l-1, 2*l+1)

def hydrogenwave(x, y, z, n, l, m):
    r = np.sqrt(x**2+ y**2 + z**2)
    r2 = np.sqrt(x**2 + y**2)  # XY plane radial component
    the, phi = np.arctan2(r2, z), np.arctan2(y, x)
    return radialfunc(r, n, l)*sph_harm(m, l, phi, the)

def tesseralharm(l, m, the, phi):  # We need a real basis of S^2, as we want to plot it in the real space
    if m<0:
        Y = 1j/np.sqrt(2)*(sph_harm(m, l, phi, the) - (-1)**(m)*sph_harm(m, l, phi, the))
    elif m==0:
        Y = sph_harm(m, l, phi, the)
    elif m>0:
        Y = 1/np.sqrt(2)*(sph_harm(-m, l, phi, the) + (-1)**(m)*sph_harm(m, l, phi, the))
    return Y 

def sphcart(r, th, ph):
    x, y, z = r*np.cos(ph)*np.sin(th), r*np.sin(ph)*np.sin(th), r*np.cos(th)
    return x, y, z


# PLOTS
lin = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(lin, lin)
Z = np.linspace(-10, 10, 1000)
r = np.linspace(0, 20, 1000)

n = int(input('Energy level (n): '))
l = int(input('Orbital angular momentum (l): '))
m = int(input('Spin (m): '))
theta, phi = np.linspace(0, np.pi, 1000), np.linspace(0, 2*np.pi, 1000)
The, Phi = np.meshgrid(theta, phi)
Yt = np.abs(tesseralharm(l, m, The, Phi))
R, S = np.shape(Yt)
x3, y3, z3 = sphcart(Yt, The, Phi)

distribution = lambda n, l, m: np.abs(hydrogenwave(X, Y, Z, n, l, m))**2

fig= plt.figure(figsize=(15, 4))
ax1 = fig.add_subplot(1, 3, 1)
pc = ax1.pcolormesh(X, Z, distribution(n,l,m), cmap='inferno')
fig.colorbar(pc)
ax1.set_xlabel(r'$x/a$')
ax1.set_ylabel(r'$z/a$')
ax1.set_title('Orbitals proyection')
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(r, radialfunc(r, n, l))
ax2.set_xlabel(r'$r/a$')
ax2.set_title('Radial part')
ax2.grid()
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.plot_surface(x3, y3, z3, cmap='cool', edgecolor='k')
ax3.set_xlabel(r'$x/a$')
ax3.set_ylabel(r'$y/a$')
ax3.set_zlabel(r'$z/a$')
ax3.set_title('3D Sph. Harm.')
fig.suptitle('Hydrogen Atom Wavefunctions')
plt.show()
