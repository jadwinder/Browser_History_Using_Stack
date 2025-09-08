import tkinter as tk
from tkinter import messagebox
import re
import webbrowser

# --- Core Logic Using Stacks ---
back_stack = []
forward_stack = []
current_page = ["Home"]  # Using list to make it mutable

# --- URL Validation Function ---
def is_valid_url(url):
    # Regular expression to match valid HTTP or HTTPS URLs
    regex = r'^(http://|https://)[a-zA-Z0-9-_.]+(?:\.[a-zA-Z0-9-_.]+)+.*$'
    return re.match(regex, url) is not None

# --- GUI Functions ---
def visit_page():
    new_url = url_entry.get().strip()
    if not new_url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    if not is_valid_url(new_url):
        messagebox.showwarning("Invalid URL", "Please enter a valid URL (starting with http:// or https://).")
        return

    back_stack.append(current_page[0])
    current_page[0] = new_url
    forward_stack.clear()

    # Open the page in the browser
    webbrowser.open(new_url)

    update_display()

def go_back():
    if not back_stack:
        messagebox.showinfo("Navigation", "No pages in back history.")
        return
    forward_stack.append(current_page[0])
    current_page[0] = back_stack.pop()
    update_display()

def go_forward():
    if not forward_stack:
        messagebox.showinfo("Navigation", "No pages in forward history.")
        return
    back_stack.append(current_page[0])
    current_page[0] = forward_stack.pop()
    update_display()

def update_display():
    current_label.config(text=f"Current Page: {current_page[0]}")
    back_label.config(text=f"Back Stack: {back_stack}")
    forward_label.config(text=f"Forward Stack: {forward_stack}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Browser History Navigation using Stack")
root.geometry("600x400")

title = tk.Label(root, text="Browser Navigation (Back / Forward)", font=("Arial", 16))
title.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

visit_btn = tk.Button(btn_frame, text="Visit Page", command=visit_page)
visit_btn.grid(row=0, column=0, padx=10)

back_btn = tk.Button(btn_frame, text="← Back", command=go_back)
back_btn.grid(row=0, column=1, padx=10)

forward_btn = tk.Button(btn_frame, text="→ Forward", command=go_forward)
forward_btn.grid(row=0, column=2, padx=10)

current_label = tk.Label(root, text="Current Page: Home", font=("Arial", 14))
current_label.pack(pady=10)

back_label = tk.Label(root, text="Back Stack: []", fg="blue")
back_label.pack()

forward_label = tk.Label(root, text="Forward Stack: []", fg="green")
forward_label.pack()

root.mainloop()
