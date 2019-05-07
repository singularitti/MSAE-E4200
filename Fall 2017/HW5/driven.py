#!/usr/bin/env python3
# created at Oct 17, 2017 8:27 PM by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt

omega_0 = 16
omega = 3
F_0 = 10
m = 1
gamma = 1
phi = 0
time = np.linspace(0, 50, 500)


def steady_state(t):
    return F_0 / m / \
        np.sqrt((omega**2 - omega_0**2)**2 + (2 * gamma * omega)**2) *\
        np.cos(omega * t + phi)


def transient(t):
    if t < 10:
        return 0
    else:
        og = np.sqrt(omega_0**2 - gamma**2)
        return np.exp(-gamma * t) * (10 * np.cos(og * t) + 10 * np.sin(og * t))


ss = steady_state(time)
ts = list(map(transient, time))
fig, ax = plt.subplots()
ax.plot(time, ts)
plt.show()
