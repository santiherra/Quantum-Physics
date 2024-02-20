# IMPORT PACKAGES
import numpy as np
from scipy.integrate import quad_vec
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scienceplots

plt.style.use(['science', 'no-latex'])


# FUNCTIONS 
def reintegrand1left(k, x, t, U0):
    eta = np.sqrt(U0-k**2)
    phi = np.arctan2(eta, k)
    Ir1left = np.cos(k*x-k**2*t) + np.cos(k*x+k**2*t+2*phi)
    return Ir1left

def imintegrand1left(k, x, t, U0):
    eta = np.sqrt(U0-k**2)
    phi = np.arctan2(eta, k)
    Ii1left = np.sin(k*x-k**2*t) - np.sin(k*x+k**2*t+2*phi)
    return Ii1left

def reintegrand1right(k, x, t, U0):
    eta = np.sqrt(U0-k**2)
    phi = np.arctan2(eta, k)
    Ir1right = 2*k*np.cos(k**2*t+phi)*np.exp(-eta*x)/np.sqrt(U0)
    return Ir1right

def imintegrand1right(k, x, t, U0):
    eta = np.sqrt(U0-k**2)
    phi = np.arctan2(eta, k)
    Ir1right = -2*k*np.sin(k**2*t+phi)*np.exp(-eta*x)/np.sqrt(U0)
    return Ir1right

def reintegrand2left(k, x, t, U0):
    kappa = np.sqrt(k**2-U0)
    A1 = (k-kappa)/(k+kappa)
    Ir2left = np.cos(k*x-k**2*t)+A1*np.cos(k*x+k**2*t)
    return Ir2left

def imintegrand2left(k,x, t, U0):
    kappa = np.sqrt(k**2-U0)
    A1 = (k-kappa)/(k+kappa)
    Ii2left = np.sin(k*x-k**2*t)-A1*np.sin(k*x+k**2*t)
    return Ii2left

def reintegrand2right(k, x, t, U0):
    kappa = np.sqrt(k**2-U0)
    A2 = 2*k/(k+kappa)
    Ir2right = A2*np.cos(kappa*x-k**2*t)
    return Ir2right

def imintegrand2right(k, x, t, U0):
    kappa = np.sqrt(k**2-U0)
    A2 = 2*k/(k+kappa)
    Ii2right = A2*np.sin(kappa*x-k**2*t)
    return Ii2right

def rewavepacketleft(xl, t, U0, eps):
    Irleft = quad_vec(reintegrand1left, np.sqrt(U0)-eps, np.sqrt(U0), args=(xl, t, U0))[0]+quad_vec(reintegrand2left, np.sqrt(U0), np.sqrt(U0)+eps, args=(xl, t, U0))[0]
    return Irleft

def imwavepacketleft(xl, t, U0, eps):
    Iileft = quad_vec(imintegrand1left, np.sqrt(U0)-eps, np.sqrt(U0), args=(xl, t, U0))[0]+quad_vec(imintegrand2left, np.sqrt(U0), np.sqrt(U0)+eps, args=(xl, t, U0))[0]
    return Iileft

def rewavepacketright(xr, t, U0, eps):
    Irright = quad_vec(reintegrand1right, np.sqrt(U0)-eps, np.sqrt(U0), args=(xr, t, U0))[0]+quad_vec(reintegrand2right, np.sqrt(U0), np.sqrt(U0)+eps, args=(xr, t, U0))[0]
    return Irright

def imwavepacketright(xr, t, U0, eps):
    Iiright = quad_vec(imintegrand1right, np.sqrt(U0)-eps, np.sqrt(U0), args=(xr, t, U0))[0]+quad_vec(imintegrand2right, np.sqrt(U0), np.sqrt(U0)+eps, args=(xr, t, U0))[0]
    return Iiright


# ANIMATION
xl, xr= np.linspace(-10, 0, 150), np.linspace(0, 10, 150)
x = np.concatenate((xl, xr))
U0 = 15
eps = U0*1e-2

repsi = lambda t: np.concatenate((rewavepacketleft(xl, t, U0, eps), rewavepacketright(xr, t, U0, eps)))
impsi = lambda t: np.concatenate((imwavepacketleft(xl, t, U0, eps), imwavepacketright(xr, t, U0, eps)))

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ln1, = ax.plot(x, np.heaviside(x, 0), label='$U(x)/U_0$')
ln2, = ax.plot([], [], label=r'$Re(\psi)$')
ln3, = ax.plot([], [], label=r'$Im(\psi)$')
timer = ax.text(4.5, .6, '', bbox=dict(facecolor='white', edgecolor='black'))
ax.set_ylim(-.7, 1.1)
ax.set_xlabel('x')
fig.suptitle('WAVEPACKET IN STEP POTENTIAL')
ax.grid()
ax.legend()

t = np.linspace(0, 15, 1000)

def animate(i): # Animation function
  ln2.set_data(x, repsi(t[i]))
  ln3.set_data(x, impsi(t[i]))
  timer.set_text("t' = " + str(round(t[i], 2)))
  return ln2, ln3, timer

ani = FuncAnimation(fig, animate, frames=100, interval=.10, blit=True)
plt.show()
