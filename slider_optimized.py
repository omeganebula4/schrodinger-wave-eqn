import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.widgets import Slider
# local imports
from parameters import x_num, t_num_slider, n_max, a, t_max
from calculations import Calculator

# make array of values of variables according to given parameters
n_vals = np.arange(1, n_max+1)
t_vals = np.linspace(0, t_max, t_num_slider)
x_vals = np.linspace(0, a, x_num)

def main():
    # calculate values as a matrix
    calculator = Calculator(n_vals, t_vals)
    with Pool() as pool:
        results = np.transpose(np.array(pool.map(calculator.compute_x, x_vals)), (2, 1, 0))

    # define figure size
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax2d = fig.add_subplot(1, 2, 2)
    plt.subplots_adjust(bottom=0.25)

    # find min and max to define limits of axes later
    max_y, min_y, max_z, min_z, max_norm = 0, 0, 0, 0, 0
    for i in range(t_num_slider):
        max_y = max(max(results[i][0]), max_y)
        min_y = min(min(results[i][0]), min_y)
        max_z = max(max(results[i][1]), max_z)
        min_z = min(min(results[i][1]), min_z)
        max_norm = max(max(results[i][2]), max_norm)

    # update function called on slider update
    def update():

        # clear the plots
        ax.clear()
        ax2d.clear()

        # update to new value
        t = slider_t.val

        # get values from result matrix for corresponding value of t
        index = np.where(t_vals == t)[0][0]
        y_vals = results[index][0]
        z_vals = results[index][1]
        norm_vals = results[index][2]

        # plot the points as a line graph
        ax.plot(x_vals, y_vals, z_vals, color='b', linewidth=2)
        ax2d.plot(x_vals, norm_vals, color='r', linewidth=2)

        # set parameters for 3D graph of x vs s(x,t)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title("3D Plot of (x, s(x,t))")
        ax.set_xlim(0, a)
        ax.set_ylim(min_y, max_y)
        ax.set_zlim(min_z, max_z)

        # set parameters for 2D graph of x vs |s(x,t)|²
        ax2d.set_xlabel("x")
        ax2d.set_ylabel("|s(x,t)|²")
        ax2d.set_title("2D Plot of (x, |s(x,t)|²)")
        ax2d.set_xlim(0, a)
        ax2d.set_ylim(0, max_norm)

        # re-draw the canvas
        fig.canvas.draw_idle()

    # axis for slider
    ax_t = plt.axes((0.25, 0.1, 0.65, 0.03))
    # slider parameters/limits
    slider_t = Slider(ax_t, 'Time (s)', 0, valmax=t_max, valinit=0, valstep=t_max/(t_num_slider-1))

    # call update function
    slider_t.on_changed(lambda val: update())

    # initialise
    update()

    plt.show(block=True)

if __name__ == '__main__':
    main()