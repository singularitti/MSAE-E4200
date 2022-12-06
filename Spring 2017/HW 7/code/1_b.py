#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created at 9 avr. 2017 17:49
# created by Nil-Zil

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import eigvals

gamma_1 = 1
gamma_2 = 2
a = 1


def dynamical_matrix(k):
    return np.matrix(
        [[2 * (gamma_1 + gamma_2), -2 * gamma_2 * np.exp(-k * a * 1j) - 2 * gamma_1],
         [-2 * gamma_2 * np.exp(k * a * 1j) - 2 * gamma_1, 2 * (gamma_1 + gamma_2)]]
    )


def evals(k):
    return np.real(np.sort(eigvals(dynamical_matrix(k))))


k = np.linspace(-2*np.pi / a, 2*np.pi / a, num=500)
plt.plot(k, [evals(kk) for kk in k])
plt.show()
