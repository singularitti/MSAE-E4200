import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(0,99,100)
omega_0 = 49.5
gamma = 10
m = 0.01

rho2 = 1/m**2/((omega_0**2 - omega**2)**2 + gamma**2 * omega**2)
theta = np.arctan(-gamma*omega/(omega_0**2 - omega**2))

f1 = plt.figure(figsize=(5,7))

plt.subplot(211)
plt.plot(omega, rho2, 'r')
plt.xlabel('$\omega$')
plt.ylabel('$\\rho^2$')
#plt.text(49.5, -0.001, '$\omega_0$')
new_ticks = [0, 20, 40, 49.5, 60, 80, 100]
new_tick_label = ['0', '20', '40', '$\omega_0$', '60', '80', '100']
plt.gca().set_xticks(new_ticks)
plt.gca().set_xticklabels(new_tick_label)

plt.subplot(212)
plt.plot(omega, np.mod(theta/np.pi*180, -180), 'b')
plt.xlabel('$\omega$')
plt.ylabel('$\\theta$')
#plt.text(49.5, -177, '$\omega_0$')
new_ticks = [0, 20, 40, 49.5, 60, 80, 100]
new_tick_label = ['0', '20', '40', '$\omega_0$', '60', '80', '100']
plt.gca().set_xticks(new_ticks)
plt.gca().set_xticklabels(new_tick_label)
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.1, top=0.95, hspace=0.3)
plt.show()

# plt.savefig('ddho.pdf')