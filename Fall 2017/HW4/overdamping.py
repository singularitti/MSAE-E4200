#!/usr/bin/env python3
# created at Oct 9, 2017 1:03 PM by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt

A = [-0.2, 1]
B = 0.3
gamma = 3
w0 = 1
time = np.linspace(0, 30, 500)


def x(t, A):
    return A * np.exp(-(gamma / 2 - np.sqrt(gamma**2 / 4 - w0**2)) * t) +\
        B * np.exp(-(gamma / 2 + np.sqrt(gamma**2 / 4 - w0**2)) * t)


fig, ax = plt.subplots()
ax.plot(time, x(time, A[0]), label="$A < 0$")
ax.plot(time, x(time, A[1]), label="$A > 0$")
ax.legend(loc="best")
ax.set_xlabel("$t$", fontsize=12)
ax.set_ylabel("$x(t)$", fontsize=12)
fig.savefig("overdamping.pdf")
plt.show()
