import tkinter as tk
import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo("title","enter message here")
f = ""
window = tk.Tk()

greeting = tk.Label(
    text="Hello world",
    bg="BurlyWood",
    fg="white"
    )
greeting.pack()


    


clickme = tk.Button(
    text="dont click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=onClick
    )
clickme.pack()

fname = tk.Entry()
fname.pack()
f = fname.get()

window.mainloop()