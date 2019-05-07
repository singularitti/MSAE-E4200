#!/usr/bin/env python3
# created at Oct 9, 2017 12:55 PM by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt

gamma = 0.5
w0 = 2
A0 = 1
time = np.linspace(0, 30, 500)


def x(t):
    return np.exp(-gamma / 2 * t) * (A0 * np.cos(np.sqrt(w0**2 - gamma**2 / 4) * t))


fig, ax = plt.subplots()
ax.plot(time, x(time))
ax.set_xlabel("$t$", fontsize=12)
ax.set_ylabel("$x(t)$", fontsize=12)
fig.savefig("underdamping.pdf")
plt.show()
