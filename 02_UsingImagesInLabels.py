import tkinter as tk
import tkinter.font as tkFont


root = tk.Tk()
logo = tk.PhotoImage(file='pythonLogo.png')

customFont = tkFont.Font(family='Arial', size=12)

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root, compound=tk.CENTER, padx=10, image=logo,text=explanation, font=customFont).pack(side='left')

root.mainloop()
