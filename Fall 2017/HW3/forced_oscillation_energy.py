#!/usr/bin/env python3
# created at Sep 27, 2017 12:46 AM by Nil-Zil

import matplotlib.pyplot as plt
import numpy as np


omega_0 = 2
F_0 = 1
m = 1


def C(omega):
    return F_0 / m / (omega_0**2 - omega**2)


def x(omega, t):
    return C(omega) * np.cos(omega * t)


def F(omega, t):
    return F_0 * np.cos(omega * t)


def U_average(omega):
    return 1 / 4 * omega_0**2 * F_0**2 / m / (omega_0**2 - omega**2)**2


def T_average(w):
    return 1 / 4 * w**2 * F_0**2 / m / (omega_0**2 - w**2)**2


om = np.linspace(0, 4, 500)

fig, ax = plt.subplots()
ax.plot(om, U_average(om), label="$\\langle U \\rangle$")
ax.plot(om, T_average(om), label="$\\langle T \\rangle$")
ax.plot(om, U_average(om) + T_average(om), label="$\\langle E \\rangle$")
ax.set_xlim((0, 4))
ax.set_ylim((0, 1))
ax.legend(loc='best')
ax.axhline(y=0, color='k', linewidth=1)
ax.set_xlabel("$\omega$", fontsize=12)
ax.set_ylabel("$E$", fontsize=12)
ax.set_title("$U$ and $T$ versus $\omega$ when $\omega_0 = 2$", fontsize=16)
# plt.show()
fig.savefig('c_vs_w_energy.pdf')
