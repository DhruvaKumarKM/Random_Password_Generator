import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def pass_generator():
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbols="@#$%&/\?"

    use=lower+upper+numbers+symbols
    length=8
    password="".join(random.sample(use,length))

    messagebox.showinfo("Your generated password is:", password)

root = tk.Tk()
root.title("Random_Password_Generator created by DHRUVA")
root.config(bg='maroon')
root.geometry("400x400")

generate_link = tk.Button(root, text="Generate",height=2,width=12, command=pass_generator)
generate_link.pack(pady=50)

root.mainloop()