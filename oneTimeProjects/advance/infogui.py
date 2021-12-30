import time
import tkinter
import infoapp
from tkinter import ttk


def show_data(data):
    data_frame = tkinter.Toplevel()
    text = data[1]
    main_frame = tkinter.Frame(data_frame)
    main_frame.pack(fill=tkinter.BOTH, expand=1)
    my_canvas = tkinter.Canvas(main_frame)
    my_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
    my_scroll = ttk.Scrollbar(main_frame, orient=tkinter.VERTICAL, command=my_canvas.yview)
    my_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    my_canvas.configure(yscrollcommand=my_scroll.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = tkinter.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    head_label = tkinter.Label(second_frame, text=data[0])
    head_label.grid(row=0, column=0)
    for line in range(len(text)):
        text_data_label = tkinter.Label(second_frame, text=text[line])
        text_data_label.grid(row=line+1, column=0, columnspan=1)
    # print_but = tkinter.Button(second_frame, text="print", command=send_to_file)
    data_frame.geometry("650x800")
    data_frame.title("Extracted Data About " + data[0])


def getting_data(tt, fr):
    text = tt.get()
    if text == "":
        empty_msg = tkinter.Message(fr, text="InputBox Is Empty").pack()
    else:
        data = infoapp.fetch_ex_wiki(text)
        show_data(data)


def start_pro(ss):
    ss.quit()
    text_frame = tkinter.Toplevel()
    text_input = tkinter.Entry(text_frame, width=30)
    lab = tkinter.Label(text_frame, text="").grid(row=0, column=0)
    text_input.grid(row=1, column=0, columnspan=1)
    get_text = tkinter.Button(text_frame, text="Search", padx=15, pady=7,
                              command=lambda: getting_data(text_input, text_frame))
    get_text.grid(row=1, column=1, columnspan=1)
    text_frame.title("Input-Screen")
    text_frame.geometry("270x100")
    text_frame.mainloop()


if infoapp.com_checker():
    start_frame = tkinter.Tk()
    start_button = tkinter.Button(start_frame, text="Start", command=lambda: start_pro(start_frame), padx=40, pady=20, bg="blue", fg="white")
    start_button.pack()
    start_frame.title("Data-Fetcher")
    start_frame.geometry("300x100")
    start_frame.mainloop()


else:
    root = tkinter.Tk()
    exit_label = tkinter.Label(root, text="Either You\'re Not Online Or Server Is Not Up")
    exit_label.pack()
    quit_but = tkinter.Button(root, text="Quit", command=root.quit)
    quit_but.pack()
    root.mainloop()
