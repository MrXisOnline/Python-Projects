import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import sys
import shutil

## function properties maker
def make_func_properties(expression):
    add_term = lambda power, constant: {"power": power, "constant": constant}
    func_properties = []
    for i in expression.split():
        if len(i) == 1:
            try:
                num = int(i)
                func_properties.append(add_term(0, num))
            except:
                func_properties.append({"operator": i})
        else:
            xe = i.split("x")
            if len(xe) > 1:
                if len(xe[0]) != 0:
                    func_properties.append(add_term(int(xe[1][1:]), int(xe[0])))
                else:
                    func_properties.append(add_term(int(xe[1][1:]), 1))
            else:
                if xe[0][0] == "^":
                    func_properties.append(add_term(int(xe[0][1:]), 1))
                else:
                    func_properties.append(add_term(0, int(i[0][0])))
    return func_properties


## function creator
def make_function(properties):
    func_string = "lambda x: "
    for e in properties:
        if len(e) == 1:
            func_string += e["operator"]
        else:
            func_string += f"{e['constant']}*x**{e['power']}"
    return eval(func_string)


## plot images creator
def make_plots_images(function, x_range, precision):
    x_range = np.arange(-x_range, x_range, precision)
    y_range = np.array([function(i) for i in x_range])
    for i, (x, y) in enumerate(zip(x_range, y_range)):
        fig = plt.figure(figsize=(10,7))
        plt.plot([x_range.min(), x_range.max()], [0, 0], linewidth=3.0)
        plt.plot([0, 0], [y_range.min(), y_range.max()], linewidth=3.0)
        plt.scatter(x, y)
        plt.plot(x_range, y_range)
        # plt.grid(True)
        plt.savefig(f"tmp/img_{i}.png")
        plt.close(fig)


## video creation
def make_plot_video():
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter("plot.avi", fourcc, 20, (720, 504))
    # print(len(os.listdir("tmp")))
    for i in range(len(os.listdir("tmp"))):
        img = cv2.imread(os.path.join("tmp", f"img_{i}.png"))
        print(i)
        # print(img.shape); break
        video.write(img)
    
    video.release()
