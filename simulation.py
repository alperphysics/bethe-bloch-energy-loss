import numpy as np
import matplotlib.pyplot as plt

# physical constants
me = 0.511 # electron mass (MeV)
K = 0.307  # MeV mol^-1 cm^2

# material properties (Silicon)
Z = 14
A = 28.085
I = 173e-6 # Mean excitation potential (MeV)

# particle properties
z = 1  # charge of particle

# beta range
beta = np.linspace(0.01,0.99,500)
gamma = 1/np.sqrt(1-beta**2)

# Bethe-Bloch formula
dEdx = K*(Z/A)*(z**2/beta**2)*(0.5*np.log((2*me*beta**2*gamma**2)/I)-beta**2)

plt.plot(beta*gamma,dEdx)

plt.xlabel("βγ")
plt.ylabel("dE/dx (MeV cm²/g)")
plt.title("Bethe-Bloch Energy Loss in Silicon")

plt.show()
