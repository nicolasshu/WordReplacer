import tkinter as tk

root = tk.Tk()
v = tk.IntVar()

# Initializing the choice as Python
v.set(1)

languages = [("Python",1),
             ("Perl", 2),
             ("Java", 3),
             ("C",4)]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text = 'Choose your favourite language',
         padx = 20).pack()

for val, language in enumerate(languages):
    print(language)
    tk.Radiobutton(root,
                   text = language[0],
                   padx = 20,
                   variable = v,
                   command = ShowChoice,
                   value = val).pack(anchor=tk.W)

root.mainloop()
