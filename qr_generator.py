import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
books = []

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    if title == "" or author == "" or price == "" or quantity == "":
        messagebox.showwarning("Warning", "All fields are required")
        return

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        messagebox.showwarning("Warning", "Price must be number & Quantity integer")
        return

    books.append(f"{title} | {author} | ₹{price} | Qty:{quantity}")
    messagebox.showinfo("Success", "Book added successfully")
    clear_fields()
    view_books()

def view_books():
    listbox.delete(0, tk.END)
    for book in books:
        listbox.insert(tk.END, book)

def clear_fields():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def generate_qr():
    title = title_entry.get()
    if title == "":
        messagebox.showwarning("Warning", "Enter book title to generate QR")
        return

    qr = qrcode.make(title)
    qr = qr.resize((200, 200))

    img = ImageTk.PhotoImage(qr)
    qr_label.config(image=img)
    qr_label.image = img

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Book Management with QR Code")
root.geometry("600x500")

# Labels & Entries
tk.Label(root, text="Book Title").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Author").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Price").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Quantity").grid(row=3, column=0, padx=10, pady=5)

title_entry = tk.Entry(root, width=30)
author_entry = tk.Entry(root, width=30)
price_entry = tk.Entry(root, width=30)
quantity_entry = tk.Entry(root, width=30)

title_entry.grid(row=0, column=1)
author_entry.grid(row=1, column=1)
price_entry.grid(row=2, column=1)
quantity_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Book", command=add_book).grid(row=4, column=0, pady=10)
tk.Button(root, text="Generate QR", command=generate_qr).grid(row=4, column=1)

# Listbox
listbox = tk.Listbox(root, width=60)
listbox.grid(row=5, column=0, columnspan=2, pady=10)

# QR Display
qr_label = tk.Label(root)
qr_label.grid(row=0, column=2, rowspan=6, padx=20)

root.mainloop()
