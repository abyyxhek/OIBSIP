import tkinter as tk
from tkinter import messagebox, filedialog
import string
import random

# Generate password based on user choices
def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Save password to file
def save_password():
    password = password_var.get()
    if not password:
        messagebox.showwarning("Warning", "Generate a password first!")
        return
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        file.write(password)
        file.close()
        messagebox.showinfo("Saved", "Password saved successfully!")

# Copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# UI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x320")
root.config(bg="#f0f0f0")

# Inputs
tk.Label(root, text="Password Length:", bg="#f0f0f0").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Letters", variable=letters_var, bg="#f0f0f0").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="#f0f0f0").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f0f0f0").pack(anchor="w", padx=60)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=30, justify="center", font=("Arial", 12)).pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Save to File", command=save_password).pack(pady=5)

root.mainloop()
