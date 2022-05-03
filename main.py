import tkinter as tk
import tkinter.messagebox

def showOutput(a):
    tk.messagebox.showinfo("Answer",f"The answer is {a}.")
    window.destroy()
def getInput():
    ans = int(x.get()) * int(y.get())
    return ans
window = tk.Tk()
window.geometry("400x300")
lblenterx = tk.Label(
    text="enter x:",
    bg="BurlyWood",
    fg="white"
    )
x = tk.Entry()
lblentery = tk.Label(
    text="enter y:",
    bg="BurlyWood",
    fg="white"
    )

y = tk.Entry()
clickme = tk.Button(
    text="dont click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=lambda:showOutput(getInput())
    )
x.pack()
y.pack()
clickme.pack()
lblenterx.pack()
lblentery.pack()
window.mainloop()
