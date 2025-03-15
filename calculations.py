import numpy as np
import scipy.integrate as integrate
import scipy.constants as c
from parameters import real_func, imag_func, a

class Calculator:
    def __init__(self, n_vals, t_vals):
        self.n_vals = n_vals
        self.t_vals = t_vals
        self.energies = c.hbar * (((n_vals * c.pi) / a) ** 2) / (2 * c.m_e)
        self.real_func_integrals = np.array(
            [integrate.quad(lambda u: real_func(u) * np.sin(m * c.pi * u / a), 0, a)[0] for m in n_vals])
        self.imag_func_integrals = np.array(
            [integrate.quad(lambda u: imag_func(u) * np.sin(m * c.pi * u / a), 0, a)[0] for m in n_vals])

    def compute_x(self, x):
        ti_func_real = (2 / a) * self.real_func_integrals * np.sin(self.n_vals * c.pi * x / a)
        ti_func_imag = (2 / a) * self.imag_func_integrals * np.sin(self.n_vals * c.pi * x / a)
        energy_time_matrix = np.outer(self.energies, self.t_vals)
        cosines = np.cos(energy_time_matrix)
        sines = np.sin(energy_time_matrix)
        real = ti_func_real.dot(cosines) + ti_func_imag.dot(sines)
        imag = ti_func_imag.dot(cosines) - ti_func_real.dot(sines)
        norm = real ** 2 + imag ** 2
        return (real, imag, norm)