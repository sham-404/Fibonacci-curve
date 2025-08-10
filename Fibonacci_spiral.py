import matplotlib.pyplot as plt
import numpy as np


def fibonacci(size):
    x = [1, 1]
    a = 1
    b = 1
    for _ in range(size + 1):
        c = a + b
        x.append(c)
        a = b
        b = c

    return x


# Create a function that generates arc with given radius and angle


def arc(radius, start_angle, end_angle, centre=[0, 0]):
    a, b = centre
    theta = np.linspace(start_angle, end_angle, 100)
    x = a + radius * np.cos(theta)
    y = b + radius * np.sin(theta)
    return x, y


def fibonacci_curve(size):
    phase = 2
    x = [0, 1]
    y = [0, 1]
    x_axis = []
    y_axis = []
    radius = fibonacci(size)
    r_size = 1
    loop_size = 0

    ff, gg = arc(1, np.pi, np.pi / 2, [1, 0])
    x_axis.extend(ff)
    y_axis.extend(gg)

    while loop_size != size:
        if phase % 4 == 0:
            a = min(x)
            b = max(y)

            centre = [a, b]

            a1 = (3 / 2) * np.pi
            a2 = np.pi

            f, g = arc(radius[r_size], a1, a2, centre)
            x_axis.extend(f)
            y_axis.extend(g)

            ep = a2
            end_point_x = a + round(radius[r_size] * np.cos(ep), 8)
            end_point_y = b + round(radius[r_size] * np.sin(ep), 8)

            x.append(end_point_x)
            y.append(end_point_y)

        elif phase % 3 == 0:
            a = min(x)
            b = min(y)

            centre = [a, b]

            a1 = 2 * np.pi
            a2 = (3 / 2) * np.pi

            f, g = arc(radius[r_size], a1, a2, centre)
            x_axis.extend(f)
            y_axis.extend(g)

            ep = a2
            end_point_x = a + round(radius[r_size] * np.cos(ep), 8)
            end_point_y = b + round(radius[r_size] * np.sin(ep), 8)

            x.append(end_point_x)
            y.append(end_point_y)

        elif phase % 2 == 0:
            a = max(x)
            b = min(y)

            centre = [a, b]

            a1 = np.pi / 2
            a2 = 0

            f, g = arc(radius[r_size], a1, a2, centre)
            x_axis.extend(f)
            y_axis.extend(g)

            ep = a2
            end_point_x = a + round(radius[r_size] * np.cos(ep), 8)
            end_point_y = b + round(radius[r_size] * np.sin(ep), 8)

            x.append(end_point_x)
            y.append(end_point_y)

        else:
            a = max(x)
            b = max(y)

            centre = [a, b]

            a1 = np.pi
            a2 = np.pi / 2

            f, g = arc(radius[r_size], a1, a2, centre)
            x_axis.extend(f)
            y_axis.extend(g)

            ep = a2
            end_point_x = a + round(radius[r_size] * np.cos(ep), 8)
            end_point_y = b + round(radius[r_size] * np.sin(ep), 8)

            x.append(end_point_x)
            y.append(end_point_y)

        phase += 1
        loop_size += 1
        r_size += 1
        if phase > 4:
            phase = 1

    plt.plot(x_axis, y_axis)
    plt.axis("square")
    plt.show()


fibonacci_curve(9)
