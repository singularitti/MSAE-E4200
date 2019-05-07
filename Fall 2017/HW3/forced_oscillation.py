#!/usr/bin/env python3
# created at Sep 27, 2017 12:46 AM by Nil-Zil

import matplotlib.pyplot as plt
import numpy as np


omega_0 = 2
omega = omega_0 + 0.2
F_0 = 1
m = 1


def C(omega):
    return F_0 / m / (omega_0**2 - omega**2)


def x(omega, t):
    return C(omega) * np.cos(omega * t)


def F(omega, t):
    return F_0 * np.cos(omega * t)


om = np.linspace(0, 4, 500)
time = np.linspace(0, 3 * np.pi, 500)

fig, ax = plt.subplots(1, 2, figsize=(16, 8))
ax[0].plot(om, C(om))
ax[0].axhline(y=0, color='k', linewidth=1)
ax[0].set_xlim((0, 4))
ax[0].set_ylim((-2, 2))
ax[0].set_xlabel("$\omega$", fontsize=12)
ax[0].set_ylabel("$C(\omega)$", fontsize=12)
ax[0].set_title("$C$ versus $\omega$ when $\omega_0 = 2$", fontsize=16)

ax[1].plot(time, x(omega, time), label="$x(t)$")
ax[1].plot(time, F(omega, time), label="$F(t)$")
ax[1].legend(loc='best')
ax[1].set_ylim((-2, 2))
ax[1].set_xlabel("$t$", fontsize=12)
ax[1].set_title("$C$ and $F$ when $\omega = 2.2$", fontsize=16)

plt.show()
# fig.savefig('c_vs_w.pdf')
