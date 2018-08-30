from tkinter import *
from tkinter.messagebox import *

def answer():
    showerror('Answer','Sorry, no answer available')

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes','Not yet implemented')
    else:
        showinfo('No','Quit has been canceled')

Button(text='QUIT', command=callback).pack(fill=X)
Button(text='Answer',command=answer).pack(fill=X)
mainloop()
