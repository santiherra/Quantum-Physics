# Quantum-Physics
Repository dedicated to some exact or semi-exact solutions in Quantum Mechanics.

## Usage
To use this repository you must clone it and run the 'pip install -r requirements.txt' command so that you get all the required packages with the proper versions. 
You will find multiple Python scripts each dedicated to interactive plots about a determined Quantum System.

## Contents 
* Free Particles: Particles under null potentials 
    * wavepacket.py : Gaussian distribution 

* Well Potentials: Particles under constant or infinite potential barriers
    * Nmodes_infsq.py : Distributions made by the first N modes of oscillation in an infinite square well
    * poly_infsq.py : Simulation of a particle in the infinite square well with initial state $\psi(x, 0) = g(x) = f(x)x(L-x)$. Feel free to play with different (integrable) functions $f(x)$.
    * stepbarrier_num.py : Finite difference method simulation of a wavepacket against a finite potential wall
    * stepbarrier_theo.py: Simulation of exact solution of a wavepacket in a step potential with energies concentrated around $U_0$
    * polar_inf: Animated plot with varying modes of oscillation in the circular infinite well

* Especial potentials: Particles under some of the most well-known potentials
    * harmonic.py : Animated plot with the first 5 modes of oscillation in the harmonic potential
    * hydrogen_atom : 3 figures plot for some given (n, l, m) - plane projection of the wavefunction, radial distribution, 3D representation of the Spherical Harmonics

More sections are up to come... Keep track!
