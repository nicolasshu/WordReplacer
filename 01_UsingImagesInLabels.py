import tkinter as tk
import tkinter.font as tkFont


root = tk.Tk()
logo = tk.PhotoImage(file='pythonLogo.png')

customFont = tkFont.Font(family='Arial', size=12)
w1 = tk.Label(root, image=logo).pack(side='right')
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=explanation, font=customFont).pack(side='left')

root.mainloop()
