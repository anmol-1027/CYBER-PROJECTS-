import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip
from datetime import datetime

# -----------------------------
# Generate Password
# -----------------------------
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if digit_var.get():
            characters += string.digits

        if special_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = "".join(secrets.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        strength = check_strength(password)
        strength_label.config(text="Strength: " + strength)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# -----------------------------
# Password Strength Checker
# -----------------------------
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():
    password = password_entry.get()

    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")


# -----------------------------
# Save Password to File
# -----------------------------
def save_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("saved_passwords.txt", "a") as file:
        file.write("Date & Time : " + now + "\n")
        file.write("Password    : " + password + "\n")
        file.write(strength_label.cget("text") + "\n")
        file.write("-" * 50 + "\n")

    messagebox.showinfo("Saved", "Password saved successfully!")


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Secure Password Generator",
    font=("Arial", 18, "bold"),
    fg="darkblue"
)
title.pack(pady=15)

tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12)
).pack()

length_entry = tk.Entry(
    root,
    width=10,
    justify="center",
    font=("Arial", 12)
)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Uppercase (A-Z)",
    variable=upper_var,
    font=("Arial", 11)
).pack(anchor="w", padx=140)

tk.Checkbutton(
    root,
    text="Lowercase (a-z)",
    variable=lower_var,
    font=("Arial", 11)
).pack(anchor="w", padx=140)

tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=digit_var,
    font=("Arial", 11)
).pack(anchor="w", padx=140)

tk.Checkbutton(
    root,
    text="Special Characters (!@#$%^&*)",
    variable=special_var,
    font=("Arial", 11)
).pack(anchor="w", padx=140)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22,
    command=generate_password
)
generate_btn.pack(pady=15)

password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 13),
    justify="center"
)
password_entry.pack(pady=5)

strength_label = tk.Label(
    root,
    text="Strength: ",
    font=("Arial", 12, "bold"),
    fg="red"
)
strength_label.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    bg="blue",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20,
    command=copy_password
)
copy_btn.pack(pady=5)

save_btn = tk.Button(
    root,
    text="Save Password",
    bg="orange",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20,
    command=save_password
)
save_btn.pack(pady=5)

tk.Label(
    root,
    text="Developed by Your Name\nCyber Security Mini Project",
    font=("Arial", 10),
    fg="gray"
).pack(side="bottom", pady=20)

root.mainloop()