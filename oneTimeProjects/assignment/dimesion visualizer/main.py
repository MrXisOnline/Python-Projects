from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import plot
import numpy as np

# def form_ncords(dim=0):
#     if dim == 0:
#         return 1
    

def plot_dimension(dim=0):
    if dim == 0:
        plot1.scatter(-10, 10, c="b")
    elif dim == 1:
        plot1.scatter([-10, 10], [10, 10], c="b")
        plot1.plot([-10, 10], [10, 10], c="b")
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
plot1.grid(True)
plot_dimension(3)
# plot1.plot(y)


app = Tk()
app.geometry("800x600")
canvas = FigureCanvasTkAgg(fig, master=app)
# , highlightthickness=2, highlightbackground="black"
canvas.get_tk_widget().place(x=20, y=20, width=760, height=380)
# toolbar = NavigationToolbar2Tk(canvas, app)
# toolbar.update()
# canvas.get_tk_widget().place(x=20, y=20, width=760, height=380)
mainloop()