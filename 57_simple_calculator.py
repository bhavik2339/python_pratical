# 57. Simple Calculator using Tkinter
import tkinter as tk

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operation.get()

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = "Cannot divide by zero" if b == 0 else a / b

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x250")

tk.Label(root, text="First Number").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Second Number").pack()
entry_b = tk.Entry(root)
entry_b.pack()

operation = tk.StringVar(value="+")
tk.OptionMenu(root, operation, "+", "-", "*", "/").pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack()
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

root.mainloop()
