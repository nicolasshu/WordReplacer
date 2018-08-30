import tkinter as tk
from tkinter import font

root = tk.Tk()
#('fangsong ti', 'fixed', 'clearlyu alternate glyphs', 'courier 10 pitch', 'open look glyph', 'bitstream charter', 'song ti', 'open look cursor', 'newspaper', 'clearlyu ligature', 'mincho', 'clearlyu devangari extra', 'clearlyu pua', 'clearlyu', 'clean', 'nil', 'clearlyu arabic', 'clearlyu devanagari', 'gothic', 'clearlyu arabic extra')

tk.Label(root, text='Red Text in Times Font',
                fg = 'red',
                font = ('Symbol')).pack()
tk.Label(root, text='Green Text in Helvetica Font',
                fg = 'light green',
                bg = 'dark green',
                font = ('Heveltica', 16)).pack()
tk.Label(root, text='Blue Text in Verdana bold',
                fg = 'blue',
                bg = 'yellow',
                font =('Verdana',17)).pack()
root.mainloop()
