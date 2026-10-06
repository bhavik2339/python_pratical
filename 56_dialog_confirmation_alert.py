# 56. Confirmation and Alert Dialogs
import tkinter as tk
from tkinter import messagebox

def confirm_action():
    answer = messagebox.askyesno("Confirmation", "Do you want to continue?")
    if answer:
        messagebox.showinfo("Result", "You selected Yes.")
    else:
        messagebox.showwarning("Result", "You selected No.")

root = tk.Tk()
root.title("Dialog Example")
root.geometry("350x180")

tk.Button(root, text="Ask Confirmation", command=confirm_action).pack(pady=50)

root.mainloop()
