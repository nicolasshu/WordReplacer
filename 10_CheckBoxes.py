import tkinter as tk

def var_states():
    print('male:   %d \nfemale: %d' % (var1.get(), var2.get()))
master = tk.Tk()

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(master, text='male', variable = var1).grid(row=0, sticky=tk.W)
tk.Checkbutton(master, text='female',variable= var2).grid(row=1, sticky=tk.W)

tk.Button(master, text='QUIT', fg='red', command = master.quit).grid(row=3, sticky=tk.W, pady=4)
tk.Button(master, text='SHOW', fg='blue', command = var_states).grid(row=4, sticky=tk.W, pady=4)
tk.mainloop()
