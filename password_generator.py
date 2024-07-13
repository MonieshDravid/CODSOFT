import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def accept_password():
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo("Password Accepted", f"Password for {username} accepted: {password}")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)

def reset_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)

def generate_and_display_password():
    length = int(length_entry.get())
    password = generate_password(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame, bg="white")
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

right_frame = tk.Frame(main_frame, bg="white")
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

tk.Label(left_frame, text="Username:", font=("Arial", 12)).pack()
username_entry = tk.Entry(left_frame, width=30, font=("Arial", 12))
username_entry.pack()

tk.Label(left_frame, text="Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(left_frame, width=5, font=("Arial", 12))
length_entry.pack()

tk.Label(left_frame, text="Password:", font=("Arial", 12)).pack()
password_entry = tk.Entry(left_frame, width=30, font=("Arial", 12))
password_entry.pack()

generate_button = tk.Button(right_frame, text="Generate Password", command=generate_and_display_password, font=("Arial", 10), height=2, width=15)
generate_button.pack(fill="x")

accept_button = tk.Button(right_frame, text="Accept", command=accept_password, font=("Arial", 10), height=2, width=15)
accept_button.pack(fill="x")

reset_button = tk.Button(right_frame, text="Reset", command=reset_fields, font=("Arial", 10), height=2, width=15)
reset_button.pack(fill="x")

root.mainloop()
