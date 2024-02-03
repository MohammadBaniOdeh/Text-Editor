"""
by the students: Mohammad Mohyee Bani odeh and Hassan Braik

Dr: Ibrahim Qasrawi
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, root):
        # Initialize the text editor
        self.root = root
        self.root.title("Text Editor")

        # Create the text widget
        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Create the menu bar
        self.menu_bar = tk.Menu(self.root)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.font_var = tk.StringVar()
        self.font_menu = tk.Menu(self.format_menu, tearoff=0)
        self.font_menu.add_radiobutton(label="Arial", variable=self.font_var, value="Arial", command=self.set_font)
        self.font_menu.add_radiobutton(label="Times New Roman", variable=self.font_var, value="Times New Roman", command=self.set_font)
        self.font_menu.add_radiobutton(label="Courier New", variable=self.font_var, value="Courier New", command=self.set_font)
        self.format_menu.add_cascade(label="Font", menu=self.font_menu)
        self.font_size_var = tk.StringVar()
        self.font_size_var.set("12")  # Default font size
        self.font_size_menu = tk.Menu(self.format_menu, tearoff=0)
        self.font_size_menu.add_radiobutton(label="12", variable=self.font_size_var, value="12", command=self.set_font_size)
        self.font_size_menu.add_radiobutton(label="14", variable=self.font_size_var, value="14", command=self.set_font_size)
        self.font_size_menu.add_radiobutton(label="16", variable=self.font_size_var, value="16", command=self.set_font_size)
        self.format_menu.add_cascade(label="Font Size", menu=self.font_size_menu)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        # Configure the menu bar
        self.root.config(menu=self.menu_bar)

        # Set default font and font size
        self.font_size = 12  # Default font size
        self.text_widget.configure(font=("Arial", self.font_size))  # Default font

        # Configure event bindings for window resize and zoom
        self.root.bind('<Configure>', self.on_window_resize)

    def open_file(self):
        # Open a file and load its contents into the text widget
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert(tk.END, file.read())

    def save_file_as(self):
        # Save the contents of the text widget to a new file
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_widget.get('1.0', tk.END))

    def cut_text(self):
        # Cut the selected text from the text widget
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        # Copy the selected text from the text widget
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        # Paste the clipboard contents into the text widget
        self.text_widget.event_generate("<<Paste>>")

    def select_all(self):
        # Select all the text in the text widget
        self.text_widget.tag_add(tk.SEL, '1.0', tk.END)

    def set_font(self):
        # Set the font of the text widget
        font = self.font_var.get()
        self.text_widget.configure(font=(font, self.font_size))

    def set_font_size(self):
        # Set the font size of the text widget
        self.font_size = int(self.font_size_var.get())
        self.text_widget.configure(font=(self.font_var.get(), self.font_size))

    def on_window_resize(self, event):
        # Adjust the text widget's size to fill the available space
        self.text_widget.pack_configure(fill=tk.BOTH, expand=True)

    def create_new_window(self):
        # Create a new instance of the TextEditor in a new window
        new_window = tk.Toplevel(self.root)
        TextEditor(new_window)

root = tk.Tk()
app = TextEditor(root)
root.mainloop()
