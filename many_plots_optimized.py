import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool
# local imports
from calculations import Calculator
from parameters import x_num, n_max, t_num_plot, a, t_max

colors = ['#000000', '#0000FF', '#8A2BE2', '#A52A2A', '#D2691E', '#DC143C', '#00008B', '#008B8B', '#006400', '#8B008B', '#556B2F', '#9932CC', '#8B0000', '#483D8B', '#2F4F4F', '#2F4F4F', '#9400D3', '#FF1493', '#696969', '#696969', '#B22222', '#228B22', '#FF00FF', '#008000', '#CD5C5C', '#4B0082', '#FF00FF', '#800000', '#0000CD', '#BA55D3', '#9370DB', '#7B68EE', '#C71585', '#191970', '#000080', '#808000', '#6B8E23', '#FF4500', '#800080', '#663399', '#FF0000', '#4169E1', '#8B4513', '#2E8B57', '#A0522D', '#6A5ACD', '#708090', '#708090', '#4682B4', '#008080']

# make array of values of variables according to given parameters
x_vals = np.linspace(0, a, x_num)
t_vals = np.linspace(0, t_max, t_num_plot)
n_vals = np.arange(1, n_max+1)

def main():
    # calculate values as a matrix
    calculator = Calculator(n_vals, t_vals)
    with Pool() as pool:
        results = np.transpose(np.array(pool.map(calculator.compute_x, x_vals)), (2, 1, 0))

    # define figure size
    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax2d = fig.add_subplot(1, 2, 2)
    plt.subplots_adjust(left=0.1, right=0.8, wspace=0.6)

    # draw the line graphs with different colors for different values of t
    for i in range(len(t_vals)):
        # get values from result matrix for corresponding value of t
        y_vals = results[i][0]
        z_vals = results[i][1]
        norm_vals = results[i][2]

        # plot the points as a line graph
        ax.plot(x_vals, y_vals, z_vals, color=colors[i], linewidth=2)
        ax2d.plot(x_vals, norm_vals, color=colors[i], linewidth=2, label=f't={t_vals[i]:.1e}' if t_vals[i]!=0 else '0')

    # set parameters for 3D graph of x vs s(x,t)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("3D Plot of (x, s(x,t))")

    # set parameters for 2D graph of x vs |s(x,t)|²
    ax2d.set_xlabel("x")
    ax2d.set_ylabel("|s(x,t)|²")
    ax2d.set_title("2D Plot of (x, |s(x,t)|²)")
    ax2d.legend()
    ax2d.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

    plt.savefig('fig.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    main()