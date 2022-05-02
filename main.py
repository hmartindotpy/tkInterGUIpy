import tkinter as tk
import tkinter.messagebox

def onClick():
    f = fname.get()
    tkinter.messagebox.showinfo("hi there","hello " + f)

window = tk.Tk()

greeting = tk.Label(
    text="Hello there",
    bg="BurlyWood",
    fg="white"
    )
greeting.pack()

fname = tk.Entry()
fname.pack()

clickme = tk.Button(
    text="dont click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=onClick
    )
clickme.pack()

window.mainloop()