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
lblenterx.grid(row=0, column=0, padx=10, pady=10)
x.grid(row=0, column=1, pady=10)
lblentery.grid(row=1, column=0, padx=10, pady=10)
y.grid(row=1, column=1, pady=10)
clickme.grid(row=0, column=2, padx=10, pady=10, rowspan=2)


window.mainloop()
