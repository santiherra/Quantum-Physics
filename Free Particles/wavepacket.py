# PACKAGES
import numpy as np
import scipy as spe
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scienceplots

plt.style.use(['science', 'no-latex'])

# FUNCTIONS
def wavepack(x, t, alph=1):
    func = np.sqrt(2*alph/np.pi)/np.sqrt(1+t**2)*np.exp(-alph*x**2/(1+t**2))
    return func

def dispersion(t, alph):
    disp = (1+t**2)/(4*alph)
    return disp


# ANIMATION
x = np.linspace(-3, 3, 100)
t = np.linspace(0, 3, 80)
alph1, alph2, alph3 = .4,.7, 1

fig, ax = plt.subplots(1, 2, figsize = (8,4))
ln1, = ax[0].plot([], [], label=r'$\alpha = 0.4$')
ln2, = ax[0].plot([], [], label=r'$\alpha = 0.7$')
ln3, = ax[0].plot([], [], label=r'$\alpha = 1$')
l1, = ax[1].plot([], [], label=r'$\alpha = 0.4$')
l2, = ax[1].plot([], [], label=r'$\alpha = 0.7$')
l3, = ax[1].plot([], [], label=r'$\alpha = 1$')
fig.suptitle('Quantum Wave Packet')
ax[0].set_xlim(min(x),max(x))
ax[0].set_ylim(-.5, 1)
ax[0].set_title(r"Prob. dist.")
ax[0].set_xlabel("x'")
ax[0].set_ylabel(r"$|\psi(x,t)|^2$")
ax[1].set_xlim(min(t),max(t))
ax[1].set_ylim(.2, max(dispersion(t, alph1)))
ax[1].set_title(r"Dispersion")
ax[1].set_xlabel("t'")
ax[1].set_ylabel(r"$\sigma^2$")
ax[0].grid()
ax[0].legend()
ax[1].grid()
ax[1].legend()
n = len(t)

def animate(i): 
  ln1.set_data(x, wavepack(x, t[i], alph1))
  ln2.set_data(x, wavepack(x, t[i], alph2))
  ln3.set_data(x, wavepack(x, t[i], alph3))
  l1.set_data(t[:i+1], dispersion(t[:i+1], alph1))
  l2.set_data(t[:i+1], dispersion(t[:i+1], alph2))
  l3.set_data(t[:i+1], dispersion(t[:i+1], alph3))
  return ln1, ln2, ln3, l1, l2, l3

ani = FuncAnimation(fig, animate, frames=len(t), interval=100)
plt.show()