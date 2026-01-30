import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys


# Function to get correct path for files (works for .py and .exe)
def resource_path(filename):
    try:
        base_path = sys._MEIPASS  # Temporary folder used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)


# Main window code
root = tk.Tk()
root.title("Apna Editor")
root.geometry("800x600")

# Set window background to dark
root.configure(bg="#1e1e1e")

# Set app icon (works in both Python and EXE)
try:
    root.iconbitmap(resource_path("icon.ico"))
except:
    pass  # prevents crash if icon not found


# create text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Poppins", 12),

    # DARK MODE COLORS
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    selectbackground="#44475a"
)

text.pack(expand=True, fill=tk.BOTH)


# Main Logic

def new_file():
    text.delete(1.0, tk.END)


def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

        messagebox.showinfo("Info", "File saved successfully")


# Menu Bar

menu = tk.Menu(root, bg="#2b2b2b", fg="white",
               activebackground="#44475a", activeforeground="white")
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0, bg="#2b2b2b", fg="white",
                    activebackground="#44475a", activeforeground="white")

menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# Start the app
root.mainloop()
