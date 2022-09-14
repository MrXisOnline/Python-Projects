from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.pyplot import plot
from matplotlib.widgets import Slider
import numpy as np


def get_deg(deg):
    """take deg and returns wrt to 90, as if deg > 90 then """
    if deg <= 90:
        return deg
    else:
        return get_deg(deg - 90)


def form_cords(pre_cords, deg=0):
    """Take the previous coordinates and degree and return the new projection coordinates"""
    global cur_cords
    deg = get_deg(deg)
    if pre_cords.ndim == 0:
        return pre_cords
    elif pre_cords.ndim == 1:
        pre_cords[0][0] = 10 - 10 * (get_deg(deg) / 90)
        pre_cords[1][0] = pre_cords[0][0] + 20 * (get_deg(deg) / 90)
        return pre_cords
    elif pre_cords.ndim == 2:
        if cur_cords[0][1] <= -10:
            pre_cords[0][1] = cur_cords[0][1] + cur_cords[0][1] * (get_deg(deg) / 90)
            cur_cords = pre_cords.copy()
        elif cur_cords[0][1] <= 10:
            pre_cords[0][1] = cur_cords[0][1] - cur_cords[0][1] * (get_deg(deg) / 90)
            cur_cords = pre_cords.copy()
        return pre_cords


def plot_dimension(dim, cords: np.ndarray):
    if dim == 0:
        plot1.scatter(-10, 10, c="b")
    elif dim == 1:
        plot1.scatter(cords[0], cords[1], c="b")
        plot1.plot(cords[0], cords[1], c="b")
    elif dim == 2:
        plot1.scatter([-10, 10], [10, -10], c="b")
        plot1.scatter([-10, 10], [-20, -40], c="b")
        plot1.plot([-10, 10], [10, -10], c="b")
        plot1.plot([-10, 10], [-20, -40], c="b")
        plot1.plot([-10, -10], [10, -20], c="b")
        plot1.plot([10, 10], [-10, -40], c="b")
    elif dim == 3:
        plot1.scatter([-10, 10], [10, -10], c="b")
        plot1.scatter([-10, 10], [-20, -40], c="b")
        plot1.plot([-10, 10], [10, -10], c="b")
        plot1.plot([-10, 10], [-20, -40], c="b")
        plot1.plot([-10, -10], [10, -20], c="b")
        plot1.plot([10, 10], [-10, -40], c="b")
        plot1.scatter([20, 40], [10, -10], c="b")
        plot1.scatter([20, 40], [-20, -40], c="b")
        plot1.plot([20, 40], [10, -10], c="b")
        plot1.plot([20, 40], [-20, -40], c="b")
        plot1.plot([20, 20], [10, -20], c="b")
        plot1.plot([40, 40], [-10, -40], c="b")
        plot1.plot([-10, 20], [10, 10], c="b")
        plot1.plot([10, 40], [-10, -10], c="b")
        plot1.plot([-10, 20], [-20, -20], c="b")
        plot1.plot([10, 40], [-40, -40], c="b")


fig = Figure(figsize=(5, 5), dpi=100)
# y = np.arange(1, 100, 2)
plot1 = fig.add_subplot(111)
plot1.set_xlim(-100, 100)
plot1.set_ylim(-100, 100)
ax_time = fig.add_axes([0.12, 0.1, 0.78, 0.03])
s_time = Slider(ax_time, 'Time', 0, 359, valinit=0)
plot1.grid(True)
base_cords = np.array([[-10, 10],
                       [10, 10]])
cur_cords = base_cords.copy()
# print(dim_cords.shape)
plot_dimension(1, base_cords)
# plot1.plot(y)


def update_projection(val):
    pos = s_time.val
    dim_cords = form_cords(base_cords, int(pos))
    plot1.clear()
    plot1.set_xlim(-100, 100)
    plot1.set_ylim(-100, 100)
    plot1.grid(True)
    plot_dimension(1, dim_cords)
    print(dim_cords)


s_time.on_changed(update_projection)


app = Tk()
app.geometry("800x600")
canvas = FigureCanvasTkAgg(fig, master=app)
# , highlightthickness=2, highlightbackground="black"
canvas.get_tk_widget().place(x=20, y=20, width=760, height=380)
# toolbar = NavigationToolbar2Tk(canvas, app)
# toolbar.update()
# canvas.get_tk_widget().place(x=20, y=20, width=760, height=380)

mainloop()
