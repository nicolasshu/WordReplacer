# Import the module
import tkinter as tk

# Create a root widget
#     i.e. A window with title bar and other decor by the window manager
root = tk.Tk()

# tk.Label
#     1) Name of Parent Window -> w is the child of root
#     2) text = the text to be shown
w = tk.Label(root, text='Hello Tkinter!')

# Fit the size of the window to the given text
w.pack()

# Enter the event loop
root.mainloop()
