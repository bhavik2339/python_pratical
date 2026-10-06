# 55. GUI with buttons, labels and entry fields
import tkinter as tk

def show_message():
    label_result.config(text="Hello, " + entry_name.get())

root = tk.Tk()
root.title("Simple GUI")
root.geometry("350x200")

tk.Label(root, text="Enter Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Button(root, text="Submit", command=show_message).pack(pady=10)
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
