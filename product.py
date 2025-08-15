import tkinter as tk

def multiply():
    result.config(text=float(num1.get()) * float(num2.get()))

root = tk.Tk()

num1 = tk.Entry(root)
num1.pack()

num2 = tk.Entry(root)
num2.pack()

btn = tk.Button(root, text="Multiply", command=multiply)
btn.pack()

result = tk.Label(root)
result.pack()

root.mainloop()
