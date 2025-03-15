import numpy as np
import scipy.constants as c

x_num = 200 # bigger x_num makes the curve smoother
t_num_slider = 100 # bigger t_num makes the slider smoother for slider_optimized
t_num_plot = 10 # number of plots in one figure for many_plots_optimized
n_max = 200 # bigger n_max makes the values more accurate, limited by scipy.integrate.quad()

# length of infinite potential well
a = c.physical_constants['Bohr radius'][0]
# maximum time for time evolution
t_max = 6.2e-17

#initial wave equation s(x, 0)
def real_func(x):
    if(x <= a/2):
        return (2*x/a)**3 * np.sqrt(7/a)
    else:
        return (2*(a-x)/a)**3 * np.sqrt(7/a)

def imag_func(x):
    return 0