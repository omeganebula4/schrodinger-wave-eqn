# Visualizing Wave Functions
This is a tool to visualise the time-evolution of the wave function $\Psi(x, t)$ (referred to as s(x,t) in the code) associated with a quantum state under the influence of an infinite potential square well, i.e, $V(x) = 0 \ \forall \ 0 < x < a$ and $V(x) = \infty$ otherwise.
(We assume the potential does not change with time)

It visualises the problem: Given the initial state $\Psi(x, 0)$, what is the wave function at subsequent times $\Psi(x, t)$?

The equation used to solve this is $\Psi(x, t) = \frac{2}{a} \sum_{n=1}^{\infty} \left(\int_0^a \Psi(x, 0) \sin \left(\frac{n \pi x}{a} \right) \right) \cdot \sin \left(\frac{n \pi x}{a} \right) \cdot \exp \left(\frac{-i E_n t}{\hbar} \right)$ where $E_n = \frac{n^2 \pi^2 \hbar^2}{2ma^2}$ is the energy associated with the $n$-th stationary state $\Psi_n (x, t) = \sqrt{\frac{2}{a}} \sin \left(\frac{n \pi x}{a} \right) \cdot \exp \left(\frac{-i E_n t}{\hbar} \right)$ of the standard infinite potential well problem.

## Setup
Clone this repository to your local machine. Make sure the required packages are installed.

Ensure that all files are in the same directory.

## Plotting
Both scripts (`many_plots_optimized.py` and `slider_optimized.py`) display two figures. Every graph is a _snapshot_ taken at some instant of time.

The 3D graph on the left plots $\Psi(x, t)$ as a complex number with $y-z$ plane as the Argand plane. Each point is $(x, \Re (\Psi(x, t)), \Im (\Psi(x, t)))$.

The 2D graph on the right plots $|\Psi(x, t)|^2$ vs $x$.

## Setting the Starting Wave Function
In `parameters.py`, modify the `real_func(x)` and `imag_func(x)` functions to match the real part and imaginary part of the desired initial condition $\Psi(x, 0)$.

By default, $\Psi(x, 0) = \Psi_1 (x, 0)$ (the stationary state corresponding to $n=1$).

## Setting other parameters
In `parameters.py`, you have the option to modify other variables.
```
x_num = 200 # bigger x_num makes the curve smoother
t_num_slider = 100 # number of subdivisions in the slider in slider_optimized.py. bigger t_num makes the slider smoother
t_num_plot = 5 # number of plots in one figure for many_plots_optimized, maximum 50
n_max = 200 # bigger n_max makes the values more accurate, limited by scipy.integrate.quad()

# length of infinite potential well
a = c.physical_constants['Bohr radius'][0]
# maximum time for time evolution
t_max = 3.079819178751178e-17
```
`x_num` is the number of points at which s(x, t) is evaluated for a given time.

`n_max` is the number of stationary states under consideration. It should theoretically be infinite, but for computation purposes, a large value is sufficient. Note that a very large `n_max` could result in an error due to constraints of the `scipy.integrate.quad` function.

The default `t_max` is set to $T = \frac{2 \pi}{E_n / \hbar}$ so that $\Psi_1 (x, T) = \Psi_1 (x, 0)$ which can be seen in the visualizations.

## Running the visualizations
### `slider_optimized.py`
Ensure that the package `Qt5Agg` is installed.

If it is not, run 
```
pip install Qt5Agg
```

On running the script, it will open an external window with the graphs as shown
![window1](https://github.com/user-attachments/assets/8a6acb3d-0b73-4472-aedf-2a3594564d71)
You can move the slider to watch the time evolution of the wave function. The maximum time is the same as `t_max` set in `parameters.py`.

### `many_plots_optimized.py`
This script generates `t_num_plot` line graphs on the same figure (`t_num_plot` as set in `parameters.py`) at equal time intervals between 0 and `t_max`, both inclusive (again, as set in `parameters.py`).
If you want to generate the plots for a custom array of time instants, set the `t_vals` variable in `many_plots_optimized.py` to the desired array.

Also note that `t_num_plot` or the size of the custom array should be less than or equal to 50, since that is the number of colors available.

It also saves the plots in a file named `fig.png` in the same directory. The default/example code generates the image below:
![sample](https://github.com/user-attachments/assets/316353cc-3e55-4451-86a5-34b457aeb390)
(Note that only 4 line plots for the 3D graph can be seen since the first and last ones (according to time) are coincident due to the construction of the parameters. This is also the reason why only one line is visible for the graph for $|\Psi(x, t)|^2$ vs $x$, since all of them are coincident)

### `Stationary State Probabilities.csv`
On every run, the scripts generate a `.csv` file containing the energies (in joules) of the `n_max` stationary states used in the calculations, and their corresponding probabilities. The probability associated with energy $E_n$ correspond to the probability that a measurement of the total energy of the quantum state would return the value $E_n$.

This value is calculated as $P(H = E_n) = |c_n|^2$ where $c_n = \sqrt{\frac{2}{a}} \int_0^a \Psi(x, 0) \sin \left( \frac{n \pi x}{a} \right) dx$

Note that by default, the probability of $E_1$ should be 1 and rest of them 0, which matches (approximately) with the results in ![Stationary State Probabilities.csv](https://github.com/omeganebula4/schrodinger-wave-eqn/blob/master/Stationary%20State%20Probabilities.csv).
