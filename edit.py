import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Function to resize images
def resize_image(image_path, size=(32, 32)):
    image = Image.open(image_path)
    image = image.resize(size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsizing
    return ImageTk.PhotoImage(image)

# Create main application window
main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("Notepad")

# Create main menu
main_menu = tk.Menu()


#------------------EDIT MENU ICONS--------------------------
copy_icon = resize_image("F:/Notepad app/Notepad-Application/components/Edit/edit icons/copy.png")
paste_icon = resize_image("F:/Notepad app/Notepad-Application/components/Edit/edit icons/paste.png")
cut_icon = resize_image("F:/Notepad app/Notepad-Application/components/Edit/edit icons/cut.png")
clear_icon = resize_image("F:/Notepad app/Notepad-Application/components/Edit/edit icons/clear.png")
find_icon = resize_image("F:/Notepad app/Notepad-Application/components/Edit/edit icons/find.png")

edit = tk.Menu(main_menu, tearoff=False)


#------------------EDIT MENU ITEMS--------------------------
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+c")
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+v")
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+x")
edit.add_command(label="Clear All", image=clear_icon, compound=tk.LEFT, accelerator="Ctrl+Shift+C")
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+f")


#---------------MENU CASCADE--------------------
main_menu.add_cascade(label="Edit", menu=edit)

main_application.config(menu=main_menu)
main_application.mainloop()

