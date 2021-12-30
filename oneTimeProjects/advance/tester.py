import tkinter
from tkinter import ttk
root = tkinter.Tk()
main_frame = tkinter.Frame(root).pack(fill=tkinter.BOTH, expand=1)
my_canvas = tkinter.Canvas(main_frame)
my_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
my_scroll = ttk.Scrollbar(main_frame, orient=tkinter.VERTICAL, command=my_canvas.yview)
my_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
my_canvas.configure(yscrollcommand=my_scroll.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = tkinter.Frame(my_canvas)
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
for i in range(100):
    button = tkinter.Button(second_frame, text="hello").grid(row=i, column=0)
root.mainloop()
